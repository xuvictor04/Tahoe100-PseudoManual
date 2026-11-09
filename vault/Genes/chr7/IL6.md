---
symbol: "IL6"
type: "gene"
col: 5842
ensembl_id: "ENSG00000136244"
name: "interleukin 6"
location: "7p15.3"
module: 14
arm: "+"
pooled_cpm: 46.48
n_lines_expressing: 18
n_dd_up: 15
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 42
direction_downstream: 44
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# IL6

*interleukin 6* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.21× (z +9.7, q 2e-19, up in 10 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.54× (z +6.3, q 5e-08, up in 14 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.428× (z -5.7, q 6e-06, down in 15 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INHBA]] (+0.70, fdr 7e-06), [[PTGS2]] (+0.70, fdr 7e-06), [[MSC]] (+0.68, fdr 7e-06).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 42 arrows point to it, the strongest [[CXCL3]] → it (grade B ⚠); 44 go from it, the strongest it → [[CXCL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.21×** | +9.7 | 2e-19 | 10/16 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.96×** | +7.1 | 5e-10 | 13/16 (J82, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +6.3 | 4e-08 | 4/15 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.54×** | +6.3 | 5e-08 | 14/16 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.01×** | +5.7 | 1e-06 | 16/17 (HOP62, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +4.3 | 0.002 | 8/15 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +4.2 | 0.002 | 8/16 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.004 | 10/16 (Panc 03.27, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +3.8 | 0.008 | 8/16 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.48×** | +3.8 | 0.010 | 8/16 (J82, HOP62, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 0.5 µM |  | **2.16×** | +3.7 | 0.011 | 9/16 (HOP62, RPMI-7951, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.08×** | +3.5 | 0.020 | 2/16 (RPMI-7951, HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.70×** | +3.5 | 0.024 | 9/16 (J82, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.028 | 12/16 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +3.1 | 0.067 | 12/16 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, none with an alert; shown: the 15 strongest. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.428×** | -5.7 | 6e-06 | 15/16 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.439×** | -5.6 | 8e-06 | 16/16 (HS-578T, SW 900, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.467×** | -5.1 | 5e-05 | 16/16 (HS-578T, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.494×** | -4.8 | 3e-04 | 14/16 (HS-578T, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.498×** | -4.7 | 3e-04 | 13/16 (HS-578T, SW 1088, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.518×** | -4.4 | 8e-04 | 11/16 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.653×** | -4.1 | 0.004 | 13/16 (NCI-H2030, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.561×** | -3.9 | 0.007 | 12/16 (SW 1088, HS-578T, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.564×** | -3.9 | 0.007 | 6/16 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.581×** | -3.7 | 0.014 | 15/16 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.701×** | -3.4 | 0.035 | 11/16 (HS-578T, NCI-H2030, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 5 µM |  | **0.386×** | -3.4 | 0.036 | 13/16 (HS-578T, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -3.3 | 0.036 | 16/16 (SW 900, HS-578T, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.611×** | -3.3 | 0.036 | 10/16 (HS-578T, SW 1088, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.617×** | -3.3 | 0.042 | 12/16 (HS-578T, hTERT-HPNE, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 254 | 0 | 16 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0214× (z -20.4) |
| [[SW 900 (line)]] | alt | 133 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0490× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 177 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0894× (z -12.4) |
| [[J82 (line)]] | alt | 75.8 | 7 (5 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 40.3× (z +16.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 8.13× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 269 | 1 (1 ⚠) | 5 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 11.6× (z +13.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -12.1) |
| [[A498 (line)]] | wt | 78.8 | 2 (2 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 11.0× (z +10.3) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.0717× (z -11.8) |
| [[HOP62 (line)]] | alt | 31.7 | 3 (2 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 22.3× (z +12.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 88.1× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.0792× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 86.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0642× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 215 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -14.1) |
| [[H4 (line)]] | wt | 67.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.00767× (z -19.3) |
| [[RPMI-7951 (line)]] | alt | 82.2 | 3 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 22.6× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.0803× (z -10.3) |
| [[SNU-423 (line)]] | alt | 124 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0662× (z -11.7) |
| [[SW 1088 (line)]] | alt | 556 | 0 | 3 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0163× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 72.1 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 11.0× (z +9.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.83 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.81 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.52 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INHBA]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 400 |
| [[PTGS2]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 960 |
| [[MSC]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GREM1]] | +0.68 | +0.55 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[NR3C1]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 630 |
| [[KYNU]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[STEAP1B-AS1]] | +0.67 | +0.61 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SHISAL1]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CYP1B1]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 | STRING 448 |
| [[TCIM]] | +0.62 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[CCL2]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 985 |
| [[TNIP3]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 5, C 37. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL3 activity raises IL6's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 4.75× lower at baseline in the lines without CXCL3 | 0.028 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[CTSS]] | B | CTSS activity raises IL6's level | lines that do not express CTSS (15) vs lines expressing it (35) | 5.60× lower at baseline in the lines without CTSS | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[BDKRB2]] | B | BDKRB2 activity raises IL6's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.85× lower at baseline in the lines without BDKRB2 | 0.073 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[LINC01828]] | B | LINC01828 activity raises IL6's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 4.58× lower at baseline in the lines without LINC01828 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent |
| [[GEM]] | B | GEM activity raises IL6's level | lines that do not express GEM (9) vs lines expressing it (41) | 4.34× lower at baseline in the lines without GEM | 0.085 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[COL8A1]] | C | COL8A1 activity raises IL6's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 9.53× lower at baseline in the lines without COL8A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[CCL3]] | C | CCL3 activity raises IL6's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 11.58× lower at baseline in the lines without CCL3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1; co-absent with the target |
| [[STEAP1B-AS1]] | C | STEAP1B-AS1 activity raises IL6's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 9.97× lower at baseline in the lines without STEAP1B-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[EDIL3]] | C | EDIL3 activity raises IL6's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 7.52× lower at baseline in the lines without EDIL3 | 0.002 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[RRAD]] | C | RRAD activity raises IL6's level | lines that do not express RRAD (31) vs lines expressing it (19) | 7.47× lower at baseline in the lines without RRAD | 0.004 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA; co-absent with the target |
| [[KYNU]] | C | KYNU activity raises IL6's level | lines that do not express KYNU (29) vs lines expressing it (21) | 5.66× lower at baseline in the lines without KYNU | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725; co-absent with the target |
| [[CSF2]] | C | CSF2 activity raises IL6's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 7.84× lower at baseline in the lines without CSF2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2; co-absent with the target |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 14, C 30. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | IL6 activity raises CXCL3's level | lines that do not express IL6 (32) vs lines expressing it (18) | 3.48× lower at baseline in the lines without IL6 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[CTSS]] | B | IL6 activity raises CTSS's level | lines that do not express IL6 (32) vs lines expressing it (18) | 2.91× lower at baseline in the lines without IL6 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[CXCL2]] | B | IL6 activity raises CXCL2's level | lines that do not express IL6 (32) vs lines expressing it (18) | 3.04× lower at baseline in the lines without IL6 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[IER3]] | B | IL6 activity raises IER3's level | lines that do not express IL6 (32) vs lines expressing it (18) | 1.82× lower at baseline in the lines without IL6 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[EXT1]] | B | IL6 activity raises EXT1's level | lines that do not express IL6 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without IL6 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[RMDN2-AS1]] | B | IL6 activity raises RMDN2-AS1's level | lines that do not express IL6 (32) vs lines expressing it (18) | 2.28× lower at baseline in the lines without IL6 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[LINC02605]] | B | IL6 activity raises LINC02605's level | lines that do not express IL6 (32) vs lines expressing it (18) | 2.54× lower at baseline in the lines without IL6 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[NR3C1]] | B | IL6 activity raises NR3C1's level | lines that do not express IL6 (32) vs lines expressing it (18) | 4.35× lower at baseline in the lines without IL6 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[RIPK2]] | B | IL6 activity raises RIPK2's level | lines that do not express IL6 (32) vs lines expressing it (18) | 1.91× lower at baseline in the lines without IL6 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[GEM]] | B | IL6 activity raises GEM's level | lines that do not express IL6 (32) vs lines expressing it (18) | 2.27× lower at baseline in the lines without IL6 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[FNDC3B]] | B | IL6 activity raises FNDC3B's level | lines that do not express IL6 (32) vs lines expressing it (18) | 1.88× lower at baseline in the lines without IL6 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| cells under [[Arbutin (drug)]] 5 µM | B | IL6 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express IL6 (32) vs lines expressing it (16) | the lines without IL6: 0.78× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.2, 19.7); signed map (47.9, 23.2). **Vector** length 98.0, 37.4% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.9 | +7.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +2.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.2 | -4.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -3.1 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.1 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:22,725,884-22,732,002 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IL-6, BSF2, HGF, HSF; previously IFNB2 |
| Gene groups (HGNC) | Interleukins; Interleukin 6 type cytokine family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, APOPTOSIS, UV_RESPONSE_UP, COMPLEMENT, INTERFERON_GAMMA_RESPONSE, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 29 pathways, smallest: CD163 mediating an anti-inflammatory response; MAPK1 (ERK2) activation; MAPK3 (ERK1) activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P05231](https://www.uniprot.org/uniprotkb/P05231) (Interleukin-6):

> Cytokine with a wide variety of biological functions in immunity, tissue regeneration, and metabolism. Binds to IL6R, then the complex associates to the signaling subunit IL6ST/gp130 to trigger the intracellular IL6-signaling pathway (Probable). The interaction with the membrane-bound IL6R and IL6ST stimulates 'classic signaling', whereas the binding of IL6 and soluble IL6R to IL6ST stimulates 'trans-signaling'. Alternatively, 'cluster signaling' occurs when membrane-bound IL6:IL6R complexes on …

**Summary**, from NCBI Gene [3569](https://www.ncbi.nlm.nih.gov/gene/3569):

> This gene encodes a cytokine that functions in inflammation and the maturation of B cells. In addition, the encoded protein has been shown to be an endogenous pyrogen capable of inducing fever in people with autoimmune diseases or infections. The protein is primarily produced at sites of acute and chronic inflammation, where it is secreted into the serum and induces a transcriptional inflammatory response through interleukin 6 receptor, alpha. The functioning of this gene is implicated in a …

**Accessions** — [HGNC:6018](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6018) · Entrez [3569](https://www.ncbi.nlm.nih.gov/gene/3569) · UniProt [P05231](https://www.uniprot.org/uniprotkb/P05231) · Ensembl [ENSG00000136244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136244)

## Data

Gene col 5842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5842); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5842]; `tensor/DDL_lfc|DDL_z.npy` [5842]; `embed/gene_vectors.npy` [5842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5842 or target_col == 5842). Every well: [[IL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
