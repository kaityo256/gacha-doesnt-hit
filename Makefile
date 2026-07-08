# Makefile

PANDOC := pandoc
BUILD_DIR := build
FIG_BUILD_DIR := $(BUILD_DIR)/fig
TMP_DIR := $(BUILD_DIR)/tmp

MAIN_SRC := main.tex
MAIN_BUILD := $(BUILD_DIR)/main.tex

CHAPTER_DIRS := \
	01_preface \
	02_revolving \
	03_montyhall \
	04_gacha \
	05_percolation \
	06_social \
	07_postface \
	08_origin \
	appendix_programs \
	books

CHAPTER_TEX_NAMES := $(subst _,-,$(CHAPTER_DIRS))
TEX_FILES := $(addprefix $(BUILD_DIR)/,$(addsuffix .tex,$(CHAPTER_TEX_NAMES)))

.PHONY: all tex fig pdf clean distclean list

all: pdf

tex: $(MAIN_BUILD) $(TEX_FILES)

fig: tex

pdf: fig tex
	cd $(BUILD_DIR);latexmk main

$(MAIN_BUILD): $(MAIN_SRC) | $(BUILD_DIR)
	cp $(MAIN_SRC) $(MAIN_BUILD)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(TMP_DIR):
	mkdir -p $(TMP_DIR)

$(FIG_BUILD_DIR):
	mkdir -p $(FIG_BUILD_DIR)

# 各 README.md -> build/*.tex の個別ルールを生成する
define make_chapter_rule

$(BUILD_DIR)/$(subst _,-,$(1)).tex: $(1)/README.md | $(BUILD_DIR) $(TMP_DIR) $(FIG_BUILD_DIR)
	@cp $$< $(TMP_DIR)/$(subst _,-,$(1)).md
	@if [ -d "$(1)/fig" ]; then \
		for f in "$(1)"/fig/*.png; do \
			[ -e "$$$$f" ] || continue; \
			base=$$$$(basename "$$$$f"); \
			safe_base=$$$$(printf '%s' "$$$$base" | tr '_' '-'); \
			safe_chapter="$(subst _,-,$(1))"; \
			cp "$$$$f" "$(FIG_BUILD_DIR)/$$$$safe_chapter-$$$$safe_base"; \
			perl -0pi -e "s#\\(fig/$$$$base\\)#(fig/$$$$safe_chapter-$$$$safe_base)#g" $(TMP_DIR)/$(subst _,-,$(1)).md; \
			perl -0pi -e "s#\\(\\./fig/$$$$base\\)#(fig/$$$$safe_chapter-$$$$safe_base)#g" $(TMP_DIR)/$(subst _,-,$(1)).md; \
			perl -0pi -e "s#\\($(1)/fig/$$$$base\\)#(fig/$$$$safe_chapter-$$$$safe_base)#g" $(TMP_DIR)/$(subst _,-,$(1)).md; \
		done; \
	fi
	$(PANDOC) $(TMP_DIR)/$(subst _,-,$(1)).md \
		-f markdown-auto_identifiers \
		-t latex \
		--top-level-division=chapter \
		--no-highlight \
		-o $$@

endef

$(foreach d,$(CHAPTER_DIRS),$(eval $(call make_chapter_rule,$(d))))

list:
	@echo "Chapter directories:"
	@printf '  %s\n' $(CHAPTER_DIRS)
	@echo
	@echo "Generated TeX files:"
	@printf '  %s\n' $(TEX_FILES)

clean:
	rm -f $(MAIN_BUILD)
	rm -f $(TEX_FILES)
	rm -rf $(TMP_DIR)
	rm -f $(FIG_BUILD_DIR)/*.png
	rm -f $(BUILD_DIR)/*.aux
	rm -f $(BUILD_DIR)/*.log
	rm -f $(BUILD_DIR)/*.toc
	rm -f $(BUILD_DIR)/*.out
	rm -f $(BUILD_DIR)/*.fls
	rm -f $(BUILD_DIR)/*.fdb_latexmk
	rm -f $(BUILD_DIR)/*.synctex.gz
	rm -f $(BUILD_DIR)/*.bbl
	rm -f $(BUILD_DIR)/*.bcf
	rm -f $(BUILD_DIR)/*.blg
	rm -f $(BUILD_DIR)/*.run.xml

distclean: clean
	rm -rf $(BUILD_DIR)