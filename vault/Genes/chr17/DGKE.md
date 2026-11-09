---
symbol: "DGKE"
type: "gene"
col: 7752
ensembl_id: "ENSG00000153933"
name: "diacylglycerol kinase epsilon"
location: "17q22"
module: 16
arm: "-"
pooled_cpm: 31.99
n_lines_expressing: 38
n_dd_up: 34
n_dd_down: 8
n_dd_up_clean: 27
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# DGKE

*diacylglycerol kinase epsilon* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.15× (z +29.2, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.611× (z -4.6, q 6e-04, down in 14 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL21A]] (+0.61, fdr 1e-05), [[SLC35D2]] (+0.61, fdr 2e-05), [[B3GALNT2]] (+0.58, fdr 1e-05); moves opposite to [[THRAP3]] (-0.57, fdr 3e-05), [[POGZ]] (-0.57, fdr 4e-05), [[ARAF]] (-0.56, fdr 4e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CGAS]] → it (grade B ⚠); 5 go from it, the strongest it → [[C17orf67]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.15×** | +29.2 | 0e+00 | 35/36 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.27×** | +14.8 | 0e+00 | 33/36 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +12.3 | 2e-32 | 29/36 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +11.8 | 9e-30 | 31/36 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +8.8 | 2e-16 | 25/36 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +7.7 | 8e-13 | 27/36 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +7.7 | 8e-13 | 29/36 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +7.7 | 1e-12 | 25/36 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +7.2 | 4e-11 | 21/36 (KATO III, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +7.1 | 8e-11 | 25/36 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +6.5 | 3e-09 | 23/36 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +6.5 | 4e-09 | 27/36 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.1 | 4e-08 | 21/36 (SW480, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.7 | 4e-07 | 20/32 (LoVo, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 2e-06 | 18/36 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +5.3 | 3e-06 | 17/36 (MIA PaCa-2, CHP-212, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 9e-05 | 19/36 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 3e-04 | 18/36 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.611×** | -4.6 | 6e-04 | 14/36 (RKO, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.613×** | -4.6 | 6e-04 | 17/36 (RKO, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.767×** | -4.6 | 6e-04 | 12/36 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -4.6 | 6e-04 | 2/36 (COLO 205, SW 1271) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.796×** | -4.1 | 0.004 | 10/36 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.790×** | -4.1 | 0.004 | 16/36 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.857× | -4.0 | 0.006 | 9/36 (SW 900, J82, …) | top dose only | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.808×** | -3.7 | 0.015 | 11/36 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.809×** | -3.7 | 0.015 | 13/36 (SW480, HOP62, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.812×** | -3.6 | 0.018 | 7/36 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.886× | -3.1 | 0.095 | 5/36 (NCI-H1573, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 50.4 | 4 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +14.4) | [[Tucidinostat (drug)]] 5 µM 0.506× (z -9.6) |
| [[HOP62 (line)]] | alt | 18.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.04× (z +16.6) | — |
| [[NCI-H460 (line)]] | wt | 43.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +21.5) | — |
| [[SW480 (line)]] | alt | 43.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +18.1) | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.09× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 29.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +17.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +20.4) | — |
| [[RKO (line)]] | wt | 60.0 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +11.1) | [[TAK-901 (drug)]] 5 µM 0.120× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 23.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.60× (z +18.0) | — |
| [[COLO 205 (line)]] | alt | 30.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +9.6) | — |
| [[LoVo (line)]] | wt | 54.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +17.5) | — |
| [[Panc 03.27 (line)]] | alt | 62.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +12.7) | — |
| [[SNU-1 (line)]] | wt | 91.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 30.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 28.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +13.4) | — |
| [[A549 (line)]] | wt | 33.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +17.5) | — |
| [[AsPC-1 (line)]] | alt | 34.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +14.5) | — |
| [[CHP-212 (line)]] | wt | 42.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.23× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 46.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 55.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +11.2) | — |
| [[J82 (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 19.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 30.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +14.6) | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 36.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 63.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +16.0) | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -10.5) |
| [[SW1417 (line)]] | alt | 42.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +16.3) | — |
| [[SW48 (line)]] | wt | 64.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +11.7) | — |
| [[A-172 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.97 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 61.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL21A]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SLC35D2]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[B3GALNT2]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[KCTD15]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[RILPL1]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[GARS1-DT]] | +0.55 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[HPRT1]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[C17orf67]] | +0.55 | +0.40 / +0.59 | both halves | 5e-05 | STRING 546; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[BCL2L2-PABPN1]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TMEM267]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[UBE2Q2]] | +0.53 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[AGAP3]] | +0.53 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[CCDC93]] | +0.53 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THRAP3]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[POGZ]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[ARAF]] | -0.56 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[PABIR1]] | -0.56 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[ZNF548]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[RNF40]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[EID1]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[JUNB]] | -0.49 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[HES1]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ZNF776]] | -0.48 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[KIF3B]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[CSTF2T]] | -0.47 | -0.30 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGAS]] | B | CGAS activity raises DGKE's level | lines that do not express CGAS (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without CGAS | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[C17orf67]] | C | C17orf67 activity raises DGKE's level | lines that do not express C17orf67 (3) vs lines expressing it (47) | 6.23× lower at baseline in the lines without C17orf67 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARHGAP10, IQSEC2, MBOAT2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C17orf67]] | B | DGKE activity raises C17orf67's level | lines that do not express DGKE (12) vs lines expressing it (38) | 1.77× lower at baseline in the lines without DGKE | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF1B, TNFRSF10D, HHEX; maybe low, not absent; its own permutation p |
| [[HSPE1-MOB4]] | B | DGKE activity lowers HSPE1-MOB4's level | lines that do not express DGKE (12) vs lines expressing it (38) | 1.31× higher at baseline in the lines without DGKE | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF1B, TNFRSF10D, HHEX; maybe low, not absent; its own permutation p |
| [[MSL1]] | B | DGKE activity raises MSL1's level | lines that do not express DGKE (12) vs lines expressing it (38) | 1.03× lower at baseline in the lines without DGKE | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF1B, TNFRSF10D, HHEX; maybe low, not absent; its own permutation p |
| [[GDAP1]] | B | DGKE activity lowers GDAP1's level | lines that do not express DGKE (12) vs lines expressing it (38) | 1.43× higher at baseline in the lines without DGKE | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF1B, TNFRSF10D, HHEX; maybe low, not absent; its own permutation p |
| [[TASP1]] | B | DGKE activity lowers TASP1's level | lines that do not express DGKE (12) vs lines expressing it (38) | 1.27× higher at baseline in the lines without DGKE | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF1B, TNFRSF10D, HHEX; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.431). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.2, 18.6); signed map (-22.0, 6.5). **Vector** length 89.6, 22.9% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +14.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +29.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +12.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +11.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.8 | +2.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.3 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | +7.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol kinase epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:56,834,107-56,869,567 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DAGK6, DGK |
| Gene groups (HGNC) | Diacylglycerol kinase family |
| Reactome | 6 pathways, smallest: Effects of PIP2 hydrolysis; G alpha (q) signalling events; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P52429](https://www.uniprot.org/uniprotkb/P52429) (Diacylglycerol kinase epsilon):

> Membrane-bound diacylglycerol kinase that converts diacylglycerol/DAG into phosphatidic acid/phosphatidate/PA and regulates the respective levels of these two bioactive lipids. Thereby, acts as a central switch between the signaling pathways activated by these second messengers with different cellular targets and opposite effects in numerous biological processes. Also plays an important role in the biosynthesis of complex lipids. Displays specificity for diacylglycerol substrates with an …

**Summary**, from NCBI Gene [8526](https://www.ncbi.nlm.nih.gov/gene/8526):

> Diacylglycerol kinases are thought to be involved mainly in the regeneration of phosphatidylinositol (PI) from diacylglycerol in the PI-cycle during cell signal transduction. When expressed in mammalian cells, DGK-epsilon shows specificity for arachidonyl-containing diacylglycerol. DGK-epsilon is expressed predominantly in testis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2852) · Entrez [8526](https://www.ncbi.nlm.nih.gov/gene/8526) · UniProt [P52429](https://www.uniprot.org/uniprotkb/P52429) · Ensembl [ENSG00000153933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153933)

## Data

Gene col 7752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7752); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7752]; `tensor/DDL_lfc|DDL_z.npy` [7752]; `embed/gene_vectors.npy` [7752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7752 or target_col == 7752). Every well: [[DGKE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGKE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
