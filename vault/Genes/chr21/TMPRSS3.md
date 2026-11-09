---
symbol: "TMPRSS3"
type: "gene"
col: 8309
ensembl_id: "ENSG00000160183"
name: "transmembrane serine protease 3"
location: "21q22.3"
module: 8
arm: "+"
pooled_cpm: 4.62
n_lines_expressing: 21
n_dd_up: 25
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 87
direction_downstream: 51
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TMPRSS3

*transmembrane serine protease 3* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.32× (z +10.3, q 3e-22, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.01× (z +8.8, q 4e-16, up in 15 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.600× (z -4.6, q 0.001, down in 6 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPS8L3]] (+0.72, fdr 7e-06), [[POF1B]] (+0.72, fdr 7e-06), [[TNFRSF14-AS1]] (+0.71, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 87 arrows point to it, the strongest [[COL16A1]] → it (grade B ⚠); 51 go from it, the strongest it → [[TNFRSF14-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +10.3 | 3e-22 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +8.8 | 4e-16 | 15/19 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +7.1 | 3e-10 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +6.6 | 5e-09 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.95×** | +6.0 | 3e-07 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +5.9 | 3e-07 | 14/18 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.28×** | +5.3 | 1e-05 | 1/10 (AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.26×** | +5.2 | 1e-05 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.63×** | +5.0 | 5e-05 | 11/19 (AsPC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.7 | 1e-04 | 1/18 (HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.76×** | +4.7 | 1e-04 | 2/13 (LS 180, AsPC-1) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.63×** | +4.5 | 3e-04 | 0/4 | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.02×** | +4.5 | 3e-04 | 1/15 (LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.3 | 6e-04 | 3/17 (SW1417, KATO III, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.002 | 2/17 (KATO III, SW480) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.009 | 7/19 (AsPC-1, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.56×** | +3.6 | 0.009 | 1/12 (LS 180) | inconsistent across doses | position effect removed |
| [[Oxaprozin (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.041 | 2/18 (HepG2/C3A, BT-474) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.049 | 3/19 (LS 180, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.053 | 1/17 (LoVo) | inconsistent across doses |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.056 | 1/18 (BT-474) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.089 | 1/15 (Panc 03.27) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8309.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.600×** | -4.6 | 0.001 | 6/18 (Panc 03.27, CFPAC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.600×** | -4.6 | 0.001 | 12/18 (SW480, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.615×** | -4.4 | 0.002 | 8/18 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Quinestrol (drug)]] 5 µM |  | **0.717×** | -4.3 | 0.003 | 4/19 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.634×** | -4.1 | 0.004 | 12/18 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.647×** | -3.9 | 0.008 | 10/18 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.650×** | -3.9 | 0.008 | 12/18 (SW480, Panc 03.27, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.662×** | -3.4 | 0.041 | 8/17 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.686×** | -3.4 | 0.041 | 11/17 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.698×** | -3.3 | 0.064 | 12/18 (SW480, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.701×** | -3.2 | 0.068 | 6/18 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.707×** | -3.1 | 0.082 | 6/18 (Panc 03.27, NCI-H1792, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.087 | 8/18 (Panc 03.27, Hs 766T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.712×** | -3.1 | 0.087 | 9/18 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.3 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 50.3 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.133× (z -13.0) |
| [[KATO III (line)]] | alt | 21.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -10.4) |
| [[LS 180 (line)]] | wt | 8.60 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0804× (z -11.8) |
| [[LoVo (line)]] | wt | 7.99 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -10.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -11.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[COLO 205 (line)]] | alt | 5.93 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0834× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 3.55 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0835× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 3.53 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0521× (z -8.7) |
| [[A-172 (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.812 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.438 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS8L3]] | +0.72 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[POF1B]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[TNFRSF14-AS1]] | +0.71 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[PROM1]] | +0.70 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[CLIC5]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[ABO]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[USH1C]] | +0.69 | +0.62 / +0.61 | both halves | 7e-06 | STRING 541 |
| [[ELF3]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[TMPRSS2]] | +0.68 | +0.74 / +0.59 | both halves | 7e-06 | same gene group |
| [[SLC44A4]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SLC40A1]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[GPX2]] | +0.67 | +0.74 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*87 arrows, 87 of them with an alert ⚠; grade A 0, B 15, C 72. Shown: the 12 strongest; 75 more arrows (75 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL16A1]] | B | COL16A1 activity raises TMPRSS3's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.27× lower at baseline in the lines without COL16A1 | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[LYPD6B]] | B | LYPD6B activity raises TMPRSS3's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 1.86× lower at baseline in the lines without LYPD6B | 0.034 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6 |
| [[FUT2]] | B | FUT2 activity raises TMPRSS3's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without FUT2 | 0.045 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[RBM47]] | B | RBM47 activity raises TMPRSS3's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 1.88× lower at baseline in the lines without RBM47 | 0.047 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[STYK1]] | B | STYK1 activity raises TMPRSS3's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 1.70× lower at baseline in the lines without STYK1 | 0.049 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[HNMT]] | B | HNMT activity raises TMPRSS3's level | lines that do not express HNMT (17) vs lines expressing it (33) | 2.23× lower at baseline in the lines without HNMT | 0.060 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[C11orf52]] | B | C11orf52 activity raises TMPRSS3's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.97× lower at baseline in the lines without C11orf52 | 0.062 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[LNX1]] | B | LNX1 activity raises TMPRSS3's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.12× lower at baseline in the lines without LNX1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[SMPDL3B]] | B | SMPDL3B activity raises TMPRSS3's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without SMPDL3B | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[FKBP9P1]] | B | FKBP9P1 activity raises TMPRSS3's level | lines that do not express FKBP9P1 (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without FKBP9P1 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NOD2]] | B | NOD2 activity raises TMPRSS3's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without NOD2 | 0.089 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[ENPP5]] | B | ENPP5 activity raises TMPRSS3's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.41× lower at baseline in the lines without ENPP5 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |

### Downstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 19, C 32. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF14-AS1]] | B | TMPRSS3 activity raises TNFRSF14-AS1's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without TMPRSS3 | 0.004 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[MGST2]] | B | TMPRSS3 activity strengthens MGST2's drug response | lines that do not express TMPRSS3 (21) vs lines expressing it (17) | the lines without TMPRSS3 respond 0.55× as strongly (z diff +2.72); strongest at Panobinostat 0.5 µM: 0.35x vs 0.18x (z diff +4.1) | 0.006 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2; target measured in part of the lines; artifact flags |
| [[FUT2]] | B | TMPRSS3 activity raises FUT2's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without TMPRSS3 | 0.008 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[MGST2]] | B | TMPRSS3 activity raises MGST2's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.57× lower at baseline in the lines without TMPRSS3 | 0.010 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[NOD2]] | B | TMPRSS3 activity raises NOD2's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without TMPRSS3 | 0.017 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[ASS1]] | B | TMPRSS3 activity raises ASS1's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.91× lower at baseline in the lines without TMPRSS3 | 0.020 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[LPAR5]] | B | TMPRSS3 activity raises LPAR5's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.36× lower at baseline in the lines without TMPRSS3 | 0.021 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[B3GALT5]] | B | TMPRSS3 activity raises B3GALT5's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.58× lower at baseline in the lines without TMPRSS3 | 0.057 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[TRIM2]] | B | TMPRSS3 activity raises TRIM2's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.04× lower at baseline in the lines without TMPRSS3 | 0.057 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[C11orf52]] | B | TMPRSS3 activity raises C11orf52's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 1.96× lower at baseline in the lines without TMPRSS3 | 0.063 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[LYPD6B]] | B | TMPRSS3 activity raises LYPD6B's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without TMPRSS3 | 0.067 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[BCL2L15]] | B | TMPRSS3 activity raises BCL2L15's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.16× lower at baseline in the lines without TMPRSS3 | 0.076 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.3, 52.5); signed map (60.7, 4.4). **Vector** length 62.6, 18.0% of its response variance represented; |z| ≥ 3 in 600 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.53 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +6.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +1.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -3.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane serine protease 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,371,887-42,396,091 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DFNB10, DFNB8 |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; Type II transmembrane serine proteases |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [P57727](https://www.uniprot.org/uniprotkb/P57727) (Transmembrane protease serine 3):

> Probable serine protease that plays a role in hearing. Acts as a permissive factor for cochlear hair cell survival and activation at the onset of hearing and is required for saccular hair cell survival (By similarity). Activates ENaC (in vitro).

**Summary**, from NCBI Gene [64699](https://www.ncbi.nlm.nih.gov/gene/64699):

> This gene encodes a protein that belongs to the serine protease family. The encoded protein contains a serine protease domain, a transmembrane domain, an LDL receptor-like domain, and a scavenger receptor cysteine-rich domain. Serine proteases are known to be involved in a variety of biological processes, whose malfunction often leads to human diseases and disorders. This gene was identified by its association with both congenital and childhood onset autosomal recessive deafness. This gene is …

**Accessions** — [HGNC:11877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11877) · Entrez [64699](https://www.ncbi.nlm.nih.gov/gene/64699) · UniProt [P57727](https://www.uniprot.org/uniprotkb/P57727) · Ensembl [ENSG00000160183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160183)

## Data

Gene col 8309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8309); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8309]; `tensor/DDL_lfc|DDL_z.npy` [8309]; `embed/gene_vectors.npy` [8309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8309 or target_col == 8309). Every well: [[TMPRSS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMPRSS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
