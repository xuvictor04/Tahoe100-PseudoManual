---
symbol: "EPS8L3"
type: "gene"
col: 12670
ensembl_id: "ENSG00000198758"
name: "EPS8 signaling adaptor L3"
location: "1p13.3"
module: 55
arm: "+"
pooled_cpm: 10.05
n_lines_expressing: 15
n_dd_up: 16
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 166
direction_downstream: 197
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# EPS8L3

*EPS8 signaling adaptor L3* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.79× (z +12.9, q 3e-35, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +4.4, q 0.001, up in 4 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.388× (z -9.2, q 3e-17, down in 13 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMPRSS2]] (+0.82, fdr 7e-06), [[HNF4A]] (+0.81, fdr 7e-06), [[MYO7B]] (+0.80, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 166 arrows point to it, the strongest [[NOSTRIN]] → it (grade B ⚠); 197 go from it, the strongest it → [[TLDC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.79×** | +12.9 | 3e-35 | 0/10 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +9.7 | 6e-20 | 0/8 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +8.4 | 1e-14 | 0/8 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.4 | 0.001 | 4/13 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.006 | 0/13 | inconsistent across doses |  |
| [[Darolutamide (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.007 | 0/13 | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.76×** | +3.9 | 0.008 | 6/12 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +3.8 | 0.011 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.015 | 0/13 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.015 | 0/13 | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.015 | 9/13 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.029 | 0/13 | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.4 | 0.033 | 0/12 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.033 | 0/13 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.3 | 0.035 | 1/7 (HT-29) | top dose only | noisy plate (z scaled) |
| [[Tazarotene (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.052 | 0/13 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12670.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.388×** | -9.2 | 3e-17 | 13/13 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.415×** | -8.5 | 5e-15 | 12/13 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.611×** | -4.8 | 4e-04 | 11/13 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.619×** | -4.6 | 5e-04 | 12/13 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.627×** | -4.5 | 6e-04 | 9/13 (CFPAC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.616×** | -4.5 | 6e-04 | 11/13 (HT-29, LS 180, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.642×** | -4.1 | 0.003 | 7/13 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Lonafarnib (drug)]] 0.5 µM |  | **0.612×** | -3.4 | 0.048 | 0/13 | inconsistent across doses | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.700×** | -3.2 | 0.079 | 3/13 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.719×** | -3.2 | 0.079 | 5/13 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.722×** | -3.2 | 0.080 | 13/13 (SW48, LoVo, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.714×** | -3.1 | 0.080 | 1/13 (AsPC-1) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.542×** | -3.1 | 0.085 | 9/13 (CFPAC-1, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 8 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0558× (z -12.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -10.1) |
| [[HT-29 (line)]] | alt | 40.6 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -18.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.166× (z -11.1) |
| [[LS 180 (line)]] | wt | 92.2 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -17.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.147× (z -13.8) |
| [[SW480 (line)]] | alt | 37.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -22.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.109× (z -14.6) |
| [[SW1417 (line)]] | alt | 42.6 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -11.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.270× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0897× (z -12.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.118× (z -10.9) |
| [[LoVo (line)]] | wt | 29.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.120× (z -13.2) |
| [[KATO III (line)]] | alt | 9.87 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 2.53 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0489× (z -10.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HepG2_C3A (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 10.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0689× (z -8.8) |
| [[A-172 (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.780 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.917 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS2]] | +0.82 | +0.79 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[HNF4A]] | +0.81 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.80 | +0.79 / +0.75 | both halves | 7e-06 | same gene group |
| [[EDAR]] | +0.80 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.80 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[IL20RA]] | +0.79 | +0.84 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TNFRSF14-AS1]] | +0.79 | +0.81 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.78 | +0.82 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[INPP5D]] | +0.78 | +0.74 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[INAVA]] | +0.78 | +0.85 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LINC01559]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[GPX2]] | +0.76 | +0.80 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*166 arrows, 166 of them with an alert ⚠; grade A 0, B 11, C 155. Shown: the 12 strongest; 154 more arrows (154 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOSTRIN]] | B | NOSTRIN activity raises EPS8L3's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without NOSTRIN | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[RAPGEF5]] | B | RAPGEF5 activity raises EPS8L3's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.79× lower at baseline in the lines without RAPGEF5 | 0.030 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[JUP]] | B | JUP activity raises EPS8L3's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.90× lower at baseline in the lines without JUP | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[TTC28]] | B | TTC28 activity lowers EPS8L3's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 5.67× higher at baseline in the lines without TTC28 | 0.044 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[PLEKHG1]] | B | PLEKHG1 activity raises EPS8L3's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.33× lower at baseline in the lines without PLEKHG1 | 0.051 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[LINC03041]] | B | LINC03041 activity lowers EPS8L3's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 5.16× higher at baseline in the lines without LINC03041 | 0.053 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[VILL]] | B | VILL activity raises EPS8L3's level | lines that do not express VILL (16) vs lines expressing it (34) | 2.80× lower at baseline in the lines without VILL | 0.060 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[BAIAP2L2]] | B | BAIAP2L2 activity raises EPS8L3's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 2.23× lower at baseline in the lines without BAIAP2L2 | 0.062 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises EPS8L3's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.47× lower at baseline in the lines without TJP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises EPS8L3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.53× lower at baseline in the lines without SLC44A3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[TNFRSF21]] | B | TNFRSF21 activity raises EPS8L3's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.63× lower at baseline in the lines without TNFRSF21 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[CLRN3]] | C | CLRN3 activity raises EPS8L3's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 11.98× lower at baseline in the lines without CLRN3 | 7e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |

### Downstream of this gene

*197 arrows, 197 of them with an alert ⚠; grade A 0, B 46, C 151. Shown: the 12 strongest; 185 more arrows (185 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLDC2]] | B | EPS8L3 activity raises TLDC2's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.19× lower at baseline in the lines without EPS8L3 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[BAIAP2L2]] | B | EPS8L3 activity raises BAIAP2L2's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.90× lower at baseline in the lines without EPS8L3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[EPS8L1]] | B | EPS8L3 activity raises EPS8L1's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 4.62× lower at baseline in the lines without EPS8L3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[MROH7]] | B | EPS8L3 activity raises MROH7's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.24× lower at baseline in the lines without EPS8L3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[IL22RA1]] | B | EPS8L3 activity raises IL22RA1's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.72× lower at baseline in the lines without EPS8L3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[JUP]] | B | EPS8L3 activity raises JUP's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 5.27× lower at baseline in the lines without EPS8L3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[ANXA11]] | B | EPS8L3 activity raises ANXA11's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.46× lower at baseline in the lines without EPS8L3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[NUDT4]] | B | EPS8L3 activity raises NUDT4's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 2.33× lower at baseline in the lines without EPS8L3 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[ADAP1]] | B | EPS8L3 activity raises ADAP1's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.58× lower at baseline in the lines without EPS8L3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[MYRF]] | B | EPS8L3 activity raises MYRF's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 4.13× lower at baseline in the lines without EPS8L3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[TJP2]] | B | EPS8L3 activity raises TJP2's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.66× lower at baseline in the lines without EPS8L3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[TMEM184A]] | B | EPS8L3 activity raises TMEM184A's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 2.64× lower at baseline in the lines without EPS8L3 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.878). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.1, 50.8); signed map (62.7, 9.6). **Vector** length 64.7, 28.7% of its response variance represented; |z| ≥ 3 in 325 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +4.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.1 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.8 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | EPS8 signaling adaptor L3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,750,080-109,764,027 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21522, MGC16817 |
| Gene groups (HGNC) | EPS8 signaling adaptor family; SH3 domain containing |
| Matched by | ensembl_id |

UniProt [Q8TE67](https://www.uniprot.org/uniprotkb/Q8TE67) carries no function annotation.

**Summary**, from NCBI Gene [79574](https://www.ncbi.nlm.nih.gov/gene/79574):

> This gene encodes a protein that is related to epidermal growth factor receptor pathway substrate 8 (EPS8), a substrate for the epidermal growth factor receptor. The function of this protein is unknown. Alternatively spliced transcript variants encoding different isoforms exist. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21297) · Entrez [79574](https://www.ncbi.nlm.nih.gov/gene/79574) · UniProt [Q8TE67](https://www.uniprot.org/uniprotkb/Q8TE67) · Ensembl [ENSG00000198758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198758)

## Data

Gene col 12670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12670); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12670]; `tensor/DDL_lfc|DDL_z.npy` [12670]; `embed/gene_vectors.npy` [12670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12670 or target_col == 12670). Every well: [[EPS8L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPS8L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
