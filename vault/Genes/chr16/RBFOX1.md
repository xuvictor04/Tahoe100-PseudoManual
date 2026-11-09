---
symbol: "RBFOX1"
type: "gene"
col: 1219
ensembl_id: "ENSG00000078328"
name: "RNA binding fox-1 homolog 1"
location: "16p13.3"
module: 140
arm: "+"
pooled_cpm: 23.99
n_lines_expressing: 44
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# RBFOX1

*RNA binding fox-1 homolog 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.26× (z +30.7, q 0e+00, up in 28 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.763× (z -4.1, q 0.013, down in 15 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00922]] (+0.77, fdr 7e-06), [[SLC14A2]] (+0.70, fdr 7e-06), [[SLC8A1-AS1]] (+0.67, fdr 7e-06); moves opposite to [[ARMC8]] (-0.49, fdr 4e-05).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FENDRR]] → it (grade B ⚠); 2 go from it, the strongest it → [[BMPER]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.26×** | +30.7 | 0e+00 | 28/38 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.76×** | +19.9 | 0e+00 | 22/31 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.78×** | +19.2 | 0e+00 | 8/17 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.39×** | +18.5 | 0e+00 | 36/42 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +15.4 | 0e+00 | 16/24 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.56×** | +14.1 | 5e-43 | 29/40 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +11.5 | 6e-29 | 21/40 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +9.6 | 7e-20 | 29/40 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +9.5 | 1e-19 | 22/40 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +8.5 | 2e-15 | 19/42 (A498, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.7 | 7e-13 | 16/37 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +6.7 | 1e-09 | 21/41 (A-172, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +5.6 | 1e-06 | 17/42 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.5 | 3e-04 | 9/33 (HEC-1-A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.8 | 0.005 | 4/17 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.006 | 13/42 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.019 | 4/39 (HT-29, J82, …) | top dose only | position effect removed |
| [[Sulfisoxazole (drug)]] 5 µM |  | 1.16× | +3.2 | 0.043 | 5/42 (SW480, SW48, …) | top dose only |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.043 | 2/39 (A549, HEC-1-A) | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.065 | 5/42 (SW 900, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1219.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.763×** | -4.1 | 0.013 | 15/42 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -4.1 | 0.013 | 14/42 (SNU-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.759×** | -3.8 | 0.024 | 15/38 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.846× | -3.6 | 0.053 | 14/42 (HS-578T, SNU-423, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.850× | -3.5 | 0.060 | 13/42 (SNU-423, RPMI-7951, …) | top dose only | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.816× | -3.1 | 0.21 | 10/42 (SW 1088, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 241 | 0 | 16 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.0) |
| [[SNU-1 (line)]] | wt | 131 | 0 | 15 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0840× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.122× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 7.84 | 6 (1 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 10.2× (z +15.3) | [[Pimozide (drug)]] 0.05 µM 0.0840× (z -11.6) |
| [[LoVo (line)]] | wt | 7.64 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +18.0) | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 6 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 12.3× (z +17.4) | — |
| [[SW480 (line)]] | alt | 9.31 | 5 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.14× (z +19.7) | — |
| [[HS-578T (line)]] | alt | 122 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.160× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Triamcinolone (drug)]] 5 µM 0.346× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 102 | 0 | 4 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.136× (z -10.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.149× (z -10.3) |
| [[A-427 (line)]] | wt | 12.6 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.97× (z +14.1) | [[Selinexor (drug)]] 5 µM 0.243× (z -10.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 8.54 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +15.0) | — |
| [[KATO III (line)]] | alt | 7.15 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +14.2) | — |
| [[A549 (line)]] | wt | 8.02 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +14.9) | — |
| [[C-33 A (line)]] | alt | 7.56 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.01× (z +9.1) | — |
| [[C32 (line)]] | wt | 6.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 6.93 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +15.1) | — |
| [[RKO (line)]] | wt | 6.42 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 7.37 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +9.3) | — |
| [[A-172 (line)]] | wt | 17.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.04× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 6.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.96× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 44.9 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.166× (z -10.0) |
| [[H4 (line)]] | wt | 60.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 8.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 7.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.67× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 6.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +9.7) | — |
| [[J82 (line)]] | alt | 6.52 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 6.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 7.68 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.08× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 75.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.232× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00922]] | +0.77 | +0.67 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SLC14A2]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SLC8A1-AS1]] | +0.67 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[FSTL4]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 | same gene group |
| [[AADACL2-AS1]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[AGBL1]] | +0.63 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[P4HA3]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CSMD2]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[LINC01500]] | +0.62 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[LINC02755]] | +0.62 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[GABRG3]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[COL26A1]] | +0.61 | +0.36 / +0.63 | both halves | 1e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FENDRR]] | B | FENDRR activity raises RBFOX1's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.86× lower at baseline in the lines without FENDRR | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10 |
| [[TOP2A]] | B | TOP2A activity lowers RBFOX1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CRLF2]] | B | CRLF2 activity raises RBFOX1's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 2.59× lower at baseline in the lines without CRLF2 | 0.077 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMPER]] | B | RBFOX1 activity raises BMPER's level | lines that do not express RBFOX1 (6) vs lines expressing it (44) | 3.54× lower at baseline in the lines without RBFOX1 | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC02932, ZNF474, DNAH6; maybe low, not absent |
| [[SPOCK1]] | B | RBFOX1 activity raises SPOCK1's level | lines that do not express RBFOX1 (6) vs lines expressing it (44) | 3.61× lower at baseline in the lines without RBFOX1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02932, ZNF474, DNAH6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.7, 25.7); signed map (28.7, 15.1). **Vector** length 96.9, 20.6% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +19.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +30.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +19.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +8.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.7 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.5 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.5 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -3.1 | -3.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding fox-1 homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:5,239,802-7,713,340 (+) |
| Ensembl biotype | protein_coding |
| Also known as | A2BP1, FOX-1, HRNBP1 |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes; RNA binding fox-1 homologs |
| Reactome | 2 pathways, smallest: MECP2 regulates transcription factors; Transcriptional Regulation by MECP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWB1](https://www.uniprot.org/uniprotkb/Q9NWB1) (RNA binding protein fox-1 homolog 1):

> RNA-binding protein that regulates alternative splicing events by binding to 5'-UGCAUGU-3' elements. Regulates alternative splicing of tissue-specific exons and of differentially spliced exons during erythropoiesis.

**Summary**, from NCBI Gene [54715](https://www.ncbi.nlm.nih.gov/gene/54715):

> The Fox-1 family of RNA-binding proteins is evolutionarily conserved, and regulates tissue-specific alternative splicing in metazoa. Fox-1 recognizes a (U)GCAUG stretch in regulated exons or in flanking introns. The protein binds to the C-terminus of ataxin-2 and may contribute to the restricted pathology of spinocerebellar ataxia type 2 (SCA2). Ataxin-2 is the product of the SCA2 gene which causes familial neurodegenerative diseases. Fox-1 and ataxin-2 are both localized in the trans-Golgi …

**Accessions** — [HGNC:18222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18222) · Entrez [54715](https://www.ncbi.nlm.nih.gov/gene/54715) · UniProt [Q9NWB1](https://www.uniprot.org/uniprotkb/Q9NWB1) · Ensembl [ENSG00000078328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078328)

## Data

Gene col 1219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1219); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1219]; `tensor/DDL_lfc|DDL_z.npy` [1219]; `embed/gene_vectors.npy` [1219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1219 or target_col == 1219). Every well: [[RBFOX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBFOX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
