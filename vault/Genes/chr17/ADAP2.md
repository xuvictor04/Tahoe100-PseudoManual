---
symbol: "ADAP2"
type: "gene"
col: 11488
ensembl_id: "ENSG00000184060"
name: "ArfGAP with dual PH domains 2"
location: "17q11.2"
module: 35
arm: "+"
pooled_cpm: 4.98
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ADAP2

*ArfGAP with dual PH domains 2* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.06× (z +23.4, q 0e+00, up in 28 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.535× (z -6.4, q 1e-07, down in 22 of 44 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H2030 0.154×, MIA PaCa-2 0.127×; ⚠ cell-cycle shift, explains ~32% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0702×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.172×; ⚠ toxic; cell-cycle shift, explains ~53% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PJVK]] (+0.70, fdr 1e-05), [[FEZ1]] (+0.67, fdr 7e-06), [[SRSF12]] (+0.67, fdr 7e-06); moves opposite to [[UBR7]] (-0.57, fdr 3e-05), [[POLD2]] (-0.57, fdr 2e-05), [[POLA1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FAM66C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.06×** | +23.4 | 0e+00 | 28/32 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +7.8 | 2e-12 | 11/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +7.7 | 3e-12 | 11/28 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.69×** | +7.6 | 4e-12 | 16/43 (KATO III, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +5.8 | 9e-07 | 15/36 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +5.6 | 2e-06 | 15/43 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +5.3 | 9e-06 | 11/33 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.68×** | +5.3 | 9e-06 | 13/39 (C-33 A, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +5.1 | 2e-05 | 1/13 (NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +4.7 | 1e-04 | 9/41 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.5 | 3e-04 | 1/9 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.52×** | +4.3 | 9e-04 | 12/38 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.002 | 13/38 (SW480, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.46×** | +3.9 | 0.005 | 6/43 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.024 | 7/43 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.035 | 5/39 (J82, A-172, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.068 | 5/43 (A498, A-172, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.087 | 4/32 (J82, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.094 | 8/32 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11488.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H2030 0.154×, MIA PaCa-2 0.127×; ⚠ cell-cycle shift, explains ~32% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0702×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.172×; ⚠ toxic; cell-cycle shift, explains ~53% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.535×** | -6.4 | 1e-07 | 22/44 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.598×** | -5.3 | 3e-05 | 17/41 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.600×** | -5.2 | 3e-05 | 16/27 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.744× | -3.0 | 0.31 | 10/44 (PANC-1, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 3 (2 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0702× (z -13.4) |
| [[A-427 (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.172× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[HEC-1-A (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.35 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 5.34 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0846× (z -10.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H460 (line)]] | wt | 3.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 9.19 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.101× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 2.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.58× (z +10.5) | — |
| [[SW480 (line)]] | alt | 2.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.44× (z +9.7) | — |
| [[A-172 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJVK]] | +0.70 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[FEZ1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SRSF12]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[LRRC8C-DT]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.66 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SLC27A6]] | +0.66 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[TERB1]] | +0.65 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[OOEP]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[ABCC11]] | +0.65 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PPP1R42]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBR7]] | -0.57 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[POLD2]] | -0.57 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[POLA1]] | -0.55 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM66C]] | B | FAM66C activity raises ADAP2's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 2.14× lower at baseline in the lines without FAM66C | 0.008 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[HRK]] | B | HRK activity raises ADAP2's level | lines that do not express HRK (13) vs lines expressing it (37) | 2.00× lower at baseline in the lines without HRK | 0.009 | ⚠ within organs, on part of the lines; also absent: AP3B2, BSN, ZNF71 |
| [[TOP2A]] | B | TOP2A activity lowers ADAP2's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ENTREP1]] | B | ENTREP1 activity raises ADAP2's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.86× lower at baseline in the lines without ENTREP1 | 0.028 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[PALM]] | B | PALM activity raises ADAP2's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.01× lower at baseline in the lines without PALM | 0.042 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN |
| [[FAXC]] | B | FAXC activity raises ADAP2's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.08× lower at baseline in the lines without FAXC | 0.044 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[MSI1]] | B | MSI1 activity raises ADAP2's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.98× lower at baseline in the lines without MSI1 | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[ANKRD6]] | B | ANKRD6 activity raises ADAP2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without ANKRD6 | 0.062 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (9.7, 31.0); signed map (32.0, -0.8). **Vector** length 60.9, 9.66% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +23.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.5 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +5.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.3 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.6 | -6.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.1 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.4 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with dual PH domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:30,906,344-30,959,322 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CENTA2 |
| Gene groups (HGNC) | ArfGAPs; Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPF8](https://www.uniprot.org/uniprotkb/Q9NPF8) (Arf-GAP with dual PH domain-containing protein 2):

> GTPase-activating protein for the ADP ribosylation factor family (Potential). Binds phosphatidylinositol 3,4,5-trisphosphate (PtdInsP3) and inositol 1,3,4,5-tetrakisphosphate (InsP4). Possesses a stoichiometry of two binding sites for InsP4 with identical affinity.

**Summary**, from NCBI Gene [55803](https://www.ncbi.nlm.nih.gov/gene/55803):

> The protein encoded by this gene binds beta-tubulin and increases the stability of microtubules. The encoded protein can also translocate to the cell membrane and bind phosphatidylinositol 3,4,5-trisphosphate (PtdInsP3) and inositol 1,3,4,5-tetrakisphosphate (InsP4). In addition, this protein is a GTPase-activating protein for ADP ribosylation factor 6 and may be able to block the entry of some RNA viruses. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:16487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16487) · Entrez [55803](https://www.ncbi.nlm.nih.gov/gene/55803) · UniProt [Q9NPF8](https://www.uniprot.org/uniprotkb/Q9NPF8) · Ensembl [ENSG00000184060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184060)

## Data

Gene col 11488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11488); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11488]; `tensor/DDL_lfc|DDL_z.npy` [11488]; `embed/gene_vectors.npy` [11488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11488 or target_col == 11488). Every well: [[ADAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
