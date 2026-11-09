---
symbol: "SARS1"
type: "gene"
col: 402
ensembl_id: "ENSG00000031698"
name: "seryl-tRNA synthetase 1"
location: "1p13.3"
module: 63
arm: "+"
pooled_cpm: 87.91
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 5
n_dd_up_clean: 25
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# SARS1

*seryl-tRNA synthetase 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.84× (z +8.9, q 3e-16, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.579× (z -11.3, q 7e-27, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARS1]] (+0.88, fdr 7e-06), [[AARS1]] (+0.87, fdr 7e-06), [[CARS1]] (+0.85, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PSAT1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HYOU1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.84×** | +8.9 | 3e-16 | 45/48 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +8.1 | 1e-13 | 41/48 (SW480, SHP-77, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.73×** | +8.0 | 2e-13 | 43/48 (Hs 766T, C-33 A, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.44×** | +7.5 | 1e-11 | 42/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +6.6 | 5e-09 | 40/49 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.3 | 2e-08 | 38/47 (AsPC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.34×** | +6.1 | 9e-08 | 37/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +6.0 | 2e-07 | 36/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.41×** | +5.0 | 3e-05 | 34/48 (NCI-H2030, RKO, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.87×** | +4.8 | 9e-05 | 38/48 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.25×** | +4.5 | 3e-04 | 26/49 (SNU-1, Hs 766T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.4 | 4e-04 | 32/48 (LOX-IMVI, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 5e-04 | 32/48 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 5e-04 | 29/48 (SHP-77, SNU-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 31/48 (SHP-77, C-33 A, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 27/47 (SHP-77, SNU-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.002 | 24/48 (NCI-H1792, SHP-77, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.002 | 28/48 (Hs 766T, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.579×** | -11.3 | 7e-27 | 41/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.711×** | -4.8 | 4e-04 | 29/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.817×** | -4.2 | 0.005 | 24/48 (J82, HS-578T, …) | top dose only | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -3.9 | 0.015 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.786×** | -3.5 | 0.045 | 21/48 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -3.3 | 0.086 | 23/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 121 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -13.4) |
| [[SHP-77 (line)]] | alt | 74.3 | 4 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 2.56× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 111 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -17.0) |
| [[SNU-1 (line)]] | wt | 98.9 | 2 | 1 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.26× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 53.6 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.07× (z +10.2) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.1) |
| [[H4 (line)]] | wt | 113 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.4) |
| [[HT-29 (line)]] | alt | 147 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -19.5) |
| [[J82 (line)]] | alt | 75.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -11.9) |
| [[LoVo (line)]] | wt | 105 | 1 | 1 | [[Neratinib (maleate) (drug)]] 0.5 µM 2.27× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -10.3) |
| [[SW480 (line)]] | alt | 102 | 2 | 0 | [[Artesunate (drug)]] 5 µM 1.80× (z +10.2) | — |
| [[A-172 (line)]] | wt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -14.6) |
| [[A-427 (line)]] | wt | 70.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 55.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 95.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | — |
| [[HepG2_C3A (line)]] | wt | 75.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.6) |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -8.7) |
| [[Hs 766T (line)]] | wt | 94.7 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.52× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 155 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 98.6 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.17× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 81.6 | 1 | 0 | [[Neratinib (maleate) (drug)]] 0.5 µM 2.95× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 83.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 59.7 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.96× (z +8.8) | — |
| [[NCI-H661 (line)]] | alt | 148 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -8.6) |
| [[RKO (line)]] | wt | 131 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.7) |
| [[SW 1088 (line)]] | alt | 102 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0628× (z -10.9) |
| [[SW 1271 (line)]] | alt | 71.1 | 0 | 1 | — | [[Sinomenine (drug)]] 5 µM 0.216× (z -8.8) |
| [[SW1417 (line)]] | alt | 86.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -11.6) |
| [[A498 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 92.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARS1]] | +0.88 | +0.88 / +0.86 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 975 |
| [[AARS1]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 881 |
| [[CARS1]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 913 |
| [[TRIB3]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[ASNS]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 500 |
| [[XPOT]] | +0.83 | +0.84 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[MARS1]] | +0.83 | +0.84 / +0.79 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 895 |
| [[SESN2]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[EIF2S2]] | +0.80 | +0.79 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[MTHFD2]] | +0.80 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[CHAC1]] | +0.80 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[IARS1]] | +0.79 | +0.81 / +0.76 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 908 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSAT1]] | B | PSAT1 activity raises SARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.47× lower at baseline in the lines without PSAT1 | 0.043 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[CHAC1]] | B | CHAC1 activity raises SARS1's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without CHAC1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[CTH]] | B | CTH activity raises SARS1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.39× lower at baseline in the lines without CTH | 0.056 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity raises SARS1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.24× lower at baseline in the lines without ANK2 | 0.057 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[GPD1L]] | C | GPD1L activity raises SARS1's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without GPD1L | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[SLC1A4]] | C | SLC1A4 activity raises SARS1's level | lines that do not express SLC1A4 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without SLC1A4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCNP, PSAT1, KAZN; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HYOU1]] | C | SARS1's natural level weakens HYOU1's drug response | SARS1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.36; direction not clear | 0.008 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.912). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.2, 48.2); signed map (-13.1, 24.5). **Vector** length 146, 50.9% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.66 to 20); *unfolded protein response* (hallmark, mean cos +0.73 to 11); *Response of EIF2AK1 (HRI) to heme deficiency* (reactome, mean cos +0.76 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +9.6 | +7.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +8.9 | +8.0 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +8.8 | +8.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +8.4 | +6.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +6.9 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.8 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +8.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.9 | -11.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.2 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.5 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -2.3 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | seryl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,213,918-109,238,182 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SERS; previously SARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 6 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Selenocysteine synthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P49591](https://www.uniprot.org/uniprotkb/P49591) (Serine--tRNA ligase, cytoplasmic):

> Catalyzes the attachment of serine to tRNA(Ser) in a two-step reaction: serine is first activated by ATP to form Ser-AMP and then transferred to the acceptor end of tRNA(Ser). Is probably also able to aminoacylate tRNA(Sec) with serine, to form the misacylated tRNA L-seryl-tRNA(Sec), which will be further converted into selenocysteinyl-tRNA(Sec). In the nucleus, binds to the VEGFA core promoter and prevents MYC binding and transcriptional activation by MYC. Recruits SIRT2 to the VEGFA promoter, …

**Summary**, from NCBI Gene [6301](https://www.ncbi.nlm.nih.gov/gene/6301):

> This gene belongs to the class II amino-acyl tRNA family. The encoded enzyme catalyzes the transfer of L-serine to tRNA (Ser) and is related to bacterial and yeast counterparts. Multiple alternatively spliced transcript variants have been described but the biological validity of all variants is unknown. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:10537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10537) · Entrez [6301](https://www.ncbi.nlm.nih.gov/gene/6301) · UniProt [P49591](https://www.uniprot.org/uniprotkb/P49591) · Ensembl [ENSG00000031698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000031698)

## Data

Gene col 402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 402); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 402]; `tensor/DDL_lfc|DDL_z.npy` [402]; `embed/gene_vectors.npy` [402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 402 or target_col == 402). Every well: [[SARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
