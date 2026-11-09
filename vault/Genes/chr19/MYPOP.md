---
symbol: "MYPOP"
type: "gene"
col: 10694
ensembl_id: "ENSG00000176182"
name: "Myb related transcription factor, partner of profilin"
location: "19q13.32"
module: 30
arm: "+"
pooled_cpm: 8.83
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MYPOP

*Myb related transcription factor, partner of profilin* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.76× (z +9.0, q 1e-16, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.347× (z -23.8, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP1]] (+0.79, fdr 7e-06), [[SDHAP2]] (+0.76, fdr 7e-06), [[PRUNE1]] (+0.74, fdr 7e-06); moves opposite to [[ERCC6L2]] (-0.74, fdr 7e-06), [[ST7L]] (-0.71, fdr 1e-05), [[WARS2-AS1]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +9.0 | 1e-16 | 30/46 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +8.9 | 2e-16 | 31/47 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +6.2 | 1e-07 | 22/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.9 | 4e-07 | 20/47 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 9e-05 | 14/44 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.9 | 1e-04 | 14/47 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +4.0 | 0.005 | 16/39 (LS 180, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +3.4 | 0.041 | 8/45 (A498, SW 900, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.078 | 4/47 (HOP62, J82, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.092 | 5/43 (COLO 205, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10694.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.347×** | -23.8 | 0e+00 | 42/45 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.326×** | -17.2 | 0e+00 | 42/45 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.343×** | -17.0 | 0e+00 | 37/42 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.403×** | -14.4 | 4e-45 | 37/47 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.406×** | -14.4 | 1e-44 | 37/46 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -10.6 | 4e-24 | 29/46 (NCI-H1573, SW480, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.588×** | -8.4 | 3e-15 | 23/44 (NCI-H460, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.635×** | -7.2 | 4e-11 | 22/46 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.665×** | -6.5 | 5e-09 | 21/46 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -6.3 | 2e-08 | 20/42 (HCT15, RKO, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.715×** | -4.9 | 4e-05 | 14/25 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -4.8 | 6e-05 | 19/44 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -4.8 | 7e-05 | 17/46 (SW 900, SW1417, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -4.7 | 1e-04 | 16/47 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.779×** | -4.0 | 0.003 | 8/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.6 | 0.009 | 14/44 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.024 | 11/47 (RPMI-7951, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.815×** | -3.1 | 0.053 | 6/45 (RPMI-7951, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.28 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 8.43 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0602× (z -14.7) |
| [[A498 (line)]] | wt | 7.78 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0474× (z -17.8) |
| [[A549 (line)]] | wt | 11.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -16.6) |
| [[C32 (line)]] | wt | 8.30 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0629× (z -10.3) |
| [[SNU-423 (line)]] | alt | 5.45 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0268× (z -14.5) |
| [[A-427 (line)]] | wt | 10.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0699× (z -14.3) |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.114× (z -9.1) |
| [[HOP62 (line)]] | alt | 6.16 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0197× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 6.99 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0628× (z -12.1) |
| [[PANC-1 (line)]] | alt | 5.12 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 6.70 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0737× (z -10.4) |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -12.3) |
| [[SW480 (line)]] | alt | 9.92 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.9) |
| [[A-172 (line)]] | wt | 6.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 5.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -10.6) |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.4) |
| [[Hs 766T (line)]] | wt | 5.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -11.4) |
| [[HS-578T (line)]] | alt | 9.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -9.5) |
| [[LoVo (line)]] | wt | 9.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.5) |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 9.53 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[Panc 03.27 (line)]] | alt | 9.44 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.150× (z -9.1) |
| [[RKO (line)]] | wt | 8.97 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 8.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.4) |
| [[SW48 (line)]] | wt | 12.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0280× (z -12.5) |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | +0.79 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.76 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[PRUNE1]] | +0.74 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[NFRKB]] | +0.74 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[RNF41]] | +0.74 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.73 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[NCK1]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[LRFN3]] | +0.72 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[PLD3]] | +0.71 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[SDHB]] | +0.71 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.71 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[CRYZL1]] | +0.71 | +0.63 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.74 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[ST7L]] | -0.71 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.71 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.71 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ARRDC3-AS1]] | -0.70 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | -0.69 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[CYREN]] | -0.69 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | -0.68 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[MSRA]] | -0.68 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[LPXN]] | -0.67 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[ZBED5]] | -0.67 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[CPSF2]] | -0.66 | -0.57 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MYPOP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers MYPOP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KCNK15-AS1]] | B | KCNK15-AS1 activity raises MYPOP's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 1.40× lower at baseline in the lines without KCNK15-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |
| [[POGLUT2]] | C | POGLUT2 activity raises MYPOP's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.51× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.822). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.3, -6.3); signed map (-36.5, -3.1). **Vector** length 73.9, 12.9% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.9 | +6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +9.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +8.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.6 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +5.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -17.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.9 | -23.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -14.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -17.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | Myb related transcription factor, partner of profilin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,890,023-45,902,613 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P42pop |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VE0](https://www.uniprot.org/uniprotkb/Q86VE0) (Myb-related transcription factor, partner of profilin):

> Transcriptional repressor; DNA-binding protein that specifically recognizes the core sequence 5'-YAAC[GT]G-3'. Dimerization with PFN1 reduces its DNA-binding capacity (By similarity).

**Summary**, from NCBI Gene [339344](https://www.ncbi.nlm.nih.gov/gene/339344):

> Predicted to enable DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20178) · Entrez [339344](https://www.ncbi.nlm.nih.gov/gene/339344) · UniProt [Q86VE0](https://www.uniprot.org/uniprotkb/Q86VE0) · Ensembl [ENSG00000176182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176182)

## Data

Gene col 10694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10694); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10694]; `tensor/DDL_lfc|DDL_z.npy` [10694]; `embed/gene_vectors.npy` [10694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10694 or target_col == 10694). Every well: [[MYPOP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYPOP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
