---
symbol: "CBX7"
type: "gene"
col: 1921
ensembl_id: "ENSG00000100307"
name: "chromobox 7"
location: "22q13.1"
module: 76
arm: "+"
pooled_cpm: 8.67
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 37
n_dd_up_clean: 3
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# CBX7

*chromobox 7* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.70× (z +4.7, q 0.002, up in 19 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (11 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.270× (z -15.5, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YPEL3]] (+0.70, fdr 7e-06), [[BAIAP3]] (+0.67, fdr 1e-05), [[HDAC5]] (+0.66, fdr 8e-06); moves opposite to [[UTP20]] (-0.55, fdr 3e-05), [[ST7]] (-0.54, fdr 1e-04), [[C17orf80]] (-0.54, fdr 2e-04).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +4.7 | 0.002 | 19/43 (SW480, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.042 | 14/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.051 | 12/44 (HCT15, Hs 766T, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 1.30× | +3.2 | 0.15 | 8/44 (HCT15, KATO III, …) | inconsistent across doses | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.2 | 0.15 | 8/47 (SHP-77, HOP62, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.29× | +3.1 | 0.15 | 8/45 (KATO III, HOP62, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.15 | 12/44 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.28× | +3.1 | 0.15 | 5/47 (KATO III, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1921.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.270×** | -15.5 | 0e+00 | 41/46 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.293×** | -15.1 | 0e+00 | 44/47 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.345×** | -13.1 | 5e-37 | 39/46 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.481×** | -12.7 | 6e-35 | 35/45 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.391×** | -11.6 | 6e-29 | 37/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.522×** | -11.3 | 1e-27 | 29/44 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.433×** | -10.3 | 5e-23 | 31/43 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.434×** | -10.3 | 5e-23 | 36/47 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.228×** | -9.5 | 9e-20 | 34/46 (C32, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.464×** | -9.5 | 2e-19 | 38/45 (LoVo, SW48, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.463×** | -9.1 | 4e-18 | 30/39 (C32, SNU-423, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.257×** | -8.8 | 8e-17 | 32/42 (Hs 766T, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.507×** | -7.9 | 1e-13 | 30/45 (SK-MEL-2, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.515×** | -7.9 | 2e-13 | 32/44 (C32, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.533×** | -7.7 | 4e-13 | 28/46 (C32, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.316×** | -7.4 | 4e-12 | 32/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.540×** | -7.2 | 3e-11 | 31/46 (HOP62, SW 900, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.343×** | -6.9 | 1e-10 | 29/44 (HEC-1-A, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 14.4 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +9.7) | [[Harringtonine (drug)]] 0.5 µM 0.0482× (z -15.7) |
| [[PANC-1 (line)]] | alt | 9.83 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.1) |
| [[SW480 (line)]] | alt | 8.08 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -12.7) |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 4 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.149× (z -11.7) |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0503× (z -13.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.5) |
| [[SNU-423 (line)]] | alt | 9.22 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -9.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 5.49 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.195× (z -10.1) |
| [[HT-29 (line)]] | alt | 6.95 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -9.6) |
| [[RKO (line)]] | wt | 12.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -13.5) |
| [[A-172 (line)]] | wt | 4.93 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0938× (z -9.2) |
| [[A498 (line)]] | wt | 7.89 | 0 | 1 | — | [[EX229 (drug)]] 5 µM 0.0512× (z -8.6) |
| [[HOP62 (line)]] | alt | 8.26 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -10.7) |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0956× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[KATO III (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.146× (z -10.1) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 7.62 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.152× (z -9.3) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 3.54 | 0 | 1 | — | [[Bexarotene (drug)]] 0.05 µM 0.0462× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 6.57 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0861× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 7.61 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0481× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -8.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 7.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0717× (z -11.8) |
| [[A-427 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL3]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[BAIAP3]] | +0.67 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[HDAC5]] | +0.66 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[PHF1]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 | STRING 470 |
| [[FBXL16]] | +0.65 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[RAB40B]] | +0.64 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[COQ8A]] | +0.63 | +0.39 / +0.71 | both halves | 5e-05 |  |
| [[SPSB3]] | +0.62 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[ADIPOR1]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CEP131]] | +0.61 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[WDTC1]] | +0.61 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[MPND]] | +0.60 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ST7]] | -0.54 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[C17orf80]] | -0.54 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[PRORP]] | -0.54 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[MRPS7]] | -0.52 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[CRPPA]] | -0.52 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[ARSB]] | -0.52 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[PIGW]] | -0.52 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[MED1]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[DNAJC11]] | -0.51 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[MCPH1]] | -0.51 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[MRPL35]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CBX7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.9, -47.1); signed map (-18.0, 9.8). **Vector** length 80.0, 16.4% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +4.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -15.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.6 | -7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.1 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -12.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -6.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -6.8 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -6.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | chromobox 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,120,167-39,152,680 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Chromobox family |
| Matched by | ensembl_id |

**Function**, from UniProt [O95931](https://www.uniprot.org/uniprotkb/O95931) (Chromobox protein homolog 7):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility. Promotes histone H3 trimethylation at 'Lys-9' (H3K9me3). Binds to trimethylated lysine residues in …

**Summary**, from NCBI Gene [23492](https://www.ncbi.nlm.nih.gov/gene/23492):

> This gene encodes a protein that contains the CHROMO (CHRomatin Organization MOdifier) domain. The encoded protein is a component of the Polycomb repressive complex 1 (PRC1), and is thought to control the lifespan of several normal human cells. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:1557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1557) · Entrez [23492](https://www.ncbi.nlm.nih.gov/gene/23492) · UniProt [O95931](https://www.uniprot.org/uniprotkb/O95931) · Ensembl [ENSG00000100307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100307)

## Data

Gene col 1921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1921); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1921]; `tensor/DDL_lfc|DDL_z.npy` [1921]; `embed/gene_vectors.npy` [1921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1921 or target_col == 1921). Every well: [[CBX7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBX7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
