---
symbol: "COQ8B"
type: "gene"
col: 4460
ensembl_id: "ENSG00000123815"
name: "coenzyme Q8B"
location: "19q13.2"
module: 31
arm: "+"
pooled_cpm: 19.86
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# COQ8B

*coenzyme Q8B* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.26× (z +4.4, q 0.006, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 2.53×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.420× (z -11.8, q 4e-29, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITPKC]] (+0.70, fdr 7e-06, ⚠ same locus), [[SBNO2]] (+0.59, fdr 1e-05), [[PANX1]] (+0.56, fdr 2e-05), [[CHST15]] (+0.52, fdr 4e-05); moves opposite to [[TRPC4AP]] (-0.49, fdr 5e-05), [[BRWD1]] (-0.45, fdr 5e-05), [[GJA1]] (-0.44, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4460.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 2.53×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +4.4 | 0.006 | 23/47 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.31× | +3.5 | 0.14 | 11/48 (LOX-IMVI, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.27× | +3.3 | 0.19 | 17/47 (A549, NCI-H2030, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.28 | 4/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.25× | +3.0 | 0.28 | 12/47 (A549, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4460.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.420×** | -11.8 | 4e-29 | 38/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.496×** | -9.5 | 6e-19 | 36/46 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.538×** | -8.4 | 8e-15 | 39/47 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.571×** | -7.6 | 5e-12 | 33/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.593×** | -6.8 | 1e-09 | 29/43 (SNU-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.684×** | -5.1 | 3e-05 | 23/47 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -4.6 | 4e-04 | 21/47 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -4.1 | 0.003 | 22/48 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -4.0 | 0.004 | 18/46 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.747×** | -3.9 | 0.005 | 20/48 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.751×** | -3.9 | 0.005 | 17/45 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.748×** | -3.8 | 0.007 | 14/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.011 | 14/47 (CFPAC-1, BT-474, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.830×** | -3.6 | 0.014 | 14/48 (HCT15, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.769×** | -3.6 | 0.014 | 15/47 (RPMI-7951, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.766×** | -3.5 | 0.018 | 15/47 (HS-578T, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.843× | -3.3 | 0.032 | 16/48 (RKO, A549, …) | all doses, flat |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.856× | -3.0 | 0.081 | 7/48 (C32, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 52.2 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0802× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -9.9) |
| [[SW480 (line)]] | alt | 23.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -11.2) |
| [[A549 (line)]] | wt | 30.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0654× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 26.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 24.1 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -9.8) |
| [[SW1417 (line)]] | alt | 22.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.201× (z -9.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -9.4) |
| [[H4 (line)]] | wt | 14.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0629× (z -10.4) |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.155× (z -9.8) |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 1 | — | [[ERK5-IN-2 (drug)]] 0.5 µM 0.0686× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0923× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.272× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -8.5) |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -10.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 53.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPKC]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SBNO2]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PANX1]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CHST15]] | +0.52 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[BCL9L]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TNS2]] | +0.50 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[SOCS3]] | +0.50 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[UBXN11]] | +0.49 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[TRIM16]] | +0.48 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[TICAM1]] | +0.48 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[UNC13D]] | +0.47 | +0.53 / +0.26 | both halves | 4e-04 |  |
| [[PLEKHG2]] | +0.46 | +0.43 / +0.45 | both halves | 4e-05 |  |
| [[GNL1]] | +0.46 | +0.47 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPC4AP]] | -0.49 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[BRWD1]] | -0.45 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[GJA1]] | -0.44 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[MTM1]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[TRIM33]] | -0.44 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[INPP4A]] | -0.42 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[FBXL20]] | -0.42 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[SLC5A3]] | -0.42 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[MRPS6]] | -0.41 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[EVI5]] | -0.41 | -0.39 / -0.37 | both halves | 7e-05 |  |
| [[SLC39A6]] | -0.41 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[TPRG1L]] | -0.40 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.307). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 7.2); signed map (8.4, 33.4). **Vector** length 81.4, 16.5% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +4.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -0.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.7 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -11.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -8.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q8B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,691,514-40,725,784 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12229, COQ8; previously ADCK4 |
| Gene groups (HGNC) | ADCK family |
| Reactome | 3 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96D53](https://www.uniprot.org/uniprotkb/Q96D53) (Atypical kinase COQ8B, mitochondrial):

> Atypical kinase involved in the biosynthesis of coenzyme Q, also named ubiquinone, an essential lipid-soluble electron transporter for aerobic cellular respiration. Its substrate specificity is still unclear: may act as a protein kinase that mediates phosphorylation of COQ3. According to other reports, acts as a small molecule kinase, possibly a lipid kinase that phosphorylates a prenyl lipid in the ubiquinone biosynthesis pathway, as suggested by its ability to bind coenzyme Q lipid …

**Summary**, from NCBI Gene [79934](https://www.ncbi.nlm.nih.gov/gene/79934):

> This gene encodes a protein with two copies of a domain found in protein kinases. The encoded protein has a complete protein kinase catalytic domain, and a truncated domain that contains only the active and binding sites of the protein kinase domain, however, it is not known whether the protein has any kinase activity. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:19041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19041) · Entrez [79934](https://www.ncbi.nlm.nih.gov/gene/79934) · UniProt [Q96D53](https://www.uniprot.org/uniprotkb/Q96D53) · Ensembl [ENSG00000123815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123815)

## Data

Gene col 4460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4460); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4460]; `tensor/DDL_lfc|DDL_z.npy` [4460]; `embed/gene_vectors.npy` [4460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4460 or target_col == 4460). Every well: [[COQ8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
