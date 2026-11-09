---
symbol: "HS6ST2"
type: "gene"
col: 10038
ensembl_id: "ENSG00000171004"
name: "heparan sulfate 6-O-sulfotransferase 2"
location: "Xq26.2"
module: 18
arm: "+"
pooled_cpm: 27.71
n_lines_expressing: 22
n_dd_up: 23
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# HS6ST2

*heparan sulfate 6-O-sulfotransferase 2* — Xq26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +18.1, q 0e+00, up in 8 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.744× (z -4.7, q 0.002, down in 2 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATIC]] (+0.66, fdr 7e-06), [[WDR77]] (+0.63, fdr 1e-05), [[WDR4]] (+0.63, fdr 1e-05); moves opposite to [[PHF1]] (-0.57, fdr 3e-05), [[ECT2L]] (-0.54, fdr 1e-05), [[PLAG1]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[MAPK8IP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +18.1 | 0e+00 | 8/20 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +16.1 | 0e+00 | 6/18 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +12.8 | 5e-35 | 6/16 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +8.4 | 6e-15 | 7/20 (NCI-H2030, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +7.9 | 3e-13 | 3/19 (SW 900, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +7.1 | 1e-10 | 8/20 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +7.0 | 2e-10 | 5/16 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.3 | 2e-08 | 5/19 (NCI-H1792, SW 900, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +6.2 | 4e-08 | 8/16 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +5.5 | 2e-06 | 4/20 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +5.1 | 2e-05 | 1/19 (H4) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.9 | 4e-05 | 10/20 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.9 | 4e-05 | 14/20 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **1.31×** | +4.6 | 2e-04 | 6/18 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 2e-04 | 4/20 (SW 900, NCI-H1573, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.002 | 11/19 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 1/20 (LoVo) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.007 | 0/20 | inconsistent across doses |  |
| [[Tazarotene (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.008 | 0/20 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.008 | 3/19 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.008 | 3/20 (SW 900, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10038.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.744×** | -4.7 | 0.002 | 2/20 (NCI-H23, C32) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.775×** | -4.4 | 0.003 | 6/20 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -4.2 | 0.004 | 2/20 (NCI-H23, NCI-H2030) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.851× | -4.1 | 0.004 | 3/20 (COLO 205, A-427, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.795×** | -4.1 | 0.004 | 11/20 (SW1417, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.804×** | -3.9 | 0.007 | 11/20 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.804×** | -3.9 | 0.007 | 11/20 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.857× | -3.8 | 0.009 | 4/20 (C32, NCI-H2030, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.823×** | -3.5 | 0.028 | 3/20 (H4, NCI-H2030, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.820×** | -3.4 | 0.033 | 5/19 (LoVo, SHP-77, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.829×** | -3.4 | 0.039 | 0/20 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.712×** | -3.2 | 0.068 | 1/19 (LoVo) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 156 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 59.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -18.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 105 | 2 (1 ⚠) | 3 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.78× (z +9.5) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.308× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.308× (z -11.0) |
| [[C-33 A (line)]] | alt | 93.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0880× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 8.94 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.07× (z +11.9) | [[Digitoxin (drug)]] 0.05 µM 0.0789× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 31.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 91.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.350× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.119× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.54 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.36 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[WDR77]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[WDR4]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NME1]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ZNF239]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ABCE1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[KCTD8]] | +0.60 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[CTPS1]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[POLR1A]] | +0.59 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MDN1]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[BYSL]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[GALNT14]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF1]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[ECT2L]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[PLAG1]] | -0.54 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[AAMDC]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RSRP1]] | -0.52 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[MXD1]] | -0.52 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[TULP3]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HS6ST2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TLL1]] | C | TLL1 activity raises HS6ST2's level | lines that do not express TLL1 (28) vs lines expressing it (22) | 3.14× lower at baseline in the lines without TLL1 | 0.022 | ⚠ within organs, on part of the lines; also absent: GUCY1A1, CDH6, COL1A1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPK8IP3]] | B | HS6ST2 activity lowers MAPK8IP3's level | lines that do not express HS6ST2 (28) vs lines expressing it (22) | 1.23× higher at baseline in the lines without HS6ST2 | 0.012 | ⚠ within organs, on part of the lines; also absent: VIPR2, CACNB2, ENSG00000257883 |
| [[NYAP2]] | B | HS6ST2 activity raises NYAP2's level | lines that do not express HS6ST2 (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without HS6ST2 | 0.062 | ⚠ within organs, on part of the lines; also absent: VIPR2, CACNB2, ENSG00000257883 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-18.0, -34.5); signed map (-2.5, -48.8). **Vector** length 61.5, 17.2% of its response variance represented; |z| ≥ 3 in 486 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +18.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +7.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +3.2 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.1 | -4.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | heparan sulfate 6-O-sulfotransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.2 — chrX:132,626,015-132,961,395 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HS6ST-2 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MM7](https://www.uniprot.org/uniprotkb/Q96MM7) (Heparan-sulfate 6-O-sulfotransferase 2):

> 6-O-sulfation enzyme which catalyzes the transfer of sulfate from 3'-phosphoadenosine 5'-phosphosulfate (PAPS) to position 6 of the N-sulfoglucosamine residue (GlcNS) of heparan sulfate.

**Summary**, from NCBI Gene [90161](https://www.ncbi.nlm.nih.gov/gene/90161):

> Heparan sulfate proteoglycans are ubiquitous components of the cell surface, extracellular matrix, and basement membranes, and interact with various ligands to influence cell growth, differentiation, adhesion, and migration. This gene encodes a member of the heparan sulfate (HS) sulfotransferase gene family, which catalyze the transfer of sulfate to HS. Different family members and isoforms are thought to synthesize heparan sulfates with tissue-specific structures and functions. Multiple …

**Accessions** — [HGNC:19133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19133) · Entrez [90161](https://www.ncbi.nlm.nih.gov/gene/90161) · UniProt [Q96MM7](https://www.uniprot.org/uniprotkb/Q96MM7) · Ensembl [ENSG00000171004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171004)

## Data

Gene col 10038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10038); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10038]; `tensor/DDL_lfc|DDL_z.npy` [10038]; `embed/gene_vectors.npy` [10038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10038 or target_col == 10038). Every well: [[HS6ST2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HS6ST2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
