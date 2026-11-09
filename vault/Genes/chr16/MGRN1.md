---
symbol: "MGRN1"
type: "gene"
col: 2277
ensembl_id: "ENSG00000102858"
name: "mahogunin ring finger 1"
location: "16p13.3"
module: 41
arm: "+"
pooled_cpm: 67.47
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# MGRN1

*mahogunin ring finger 1* — 16p13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HEC-1-A 2.45×, NCI-H1573 2.82×, SNU-423 2.27×, A549 2.06×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 5.54×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 2.04×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.712× (z -7.5, q 3e-11, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.819× (z -6.3, q 5e-08, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYK2]] (+0.60, fdr 3e-05), [[MIB2]] (+0.59, fdr 1e-05), [[CCDC9]] (+0.54, fdr 2e-05); moves opposite to [[LDHB]] (-0.46, fdr 1e-04), [[ATXN7L3B]] (-0.45, fdr 1e-04), [[FABP5]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2277.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HEC-1-A 2.45×, NCI-H1573 2.82×, SNU-423 2.27×, A549 2.06×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 5.54×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 2.04×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.0 | 3e-04 | 22/48 (HEC-1-A, NCI-H1573, …) | top dose only | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.068 | 16/48 (HT-29, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.22 | 20/48 (PANC-1, NCI-H1573, …) | top dose only | composition shift; position effect removed |
| [[Larotrectinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.22 | 12/49 (A498, KATO III, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.25 | 18/48 (KATO III, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.712×** | -7.5 | 3e-11 | 36/48 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.715×** | -7.4 | 3e-11 | 34/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.747×** | -6.5 | 2e-08 | 31/48 (A498, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -6.3 | 5e-08 | 22/48 (CFPAC-1, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.756×** | -6.0 | 3e-07 | 27/48 (A-172, AsPC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.835× | -5.7 | 1e-06 | 21/49 (AsPC-1, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -5.7 | 1e-06 | 22/48 (SNU-423, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.799×** | -5.0 | 4e-05 | 24/48 (SHP-77, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.801×** | -4.9 | 5e-05 | 29/47 (A498, J82, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.805×** | -4.6 | 2e-04 | 25/47 (H4, AsPC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.819×** | -4.4 | 5e-04 | 25/48 (HT-29, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.822×** | -4.4 | 6e-04 | 21/48 (A498, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.819×** | -4.3 | 9e-04 | 23/50 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.888× | -3.7 | 0.008 | 17/48 (Hs 766T, HEC-1-A, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.848× | -3.6 | 0.010 | 15/48 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.743×** | -3.4 | 0.021 | 15/48 (A498, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.862× | -3.2 | 0.051 | 15/49 (AN3 CA, SNU-1, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.762×** | -3.2 | 0.051 | 14/48 (SK-MEL-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.871× | -3.1 | 0.065 | 11/48 (NCI-H1792, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.874× | -3.0 | 0.075 | 16/48 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.909× | -3.0 | 0.075 | 4/48 (NCI-H1573, SHP-77, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.777×** | -2.9 | 0.090 | 11/49 (A498, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 151 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.478× (z -10.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 95.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 80.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.420× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -15.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 55.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 51.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.65× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[PANC-1 (line)]] | alt | 49.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 48.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Selinexor (drug)]] 5 µM 0.531× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 69.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 58.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +16.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 63.4 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0615× (z -12.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 68.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.382× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 81.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H596 (line)]] | alt | 63.4 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.117× (z -10.7) |
| [[RKO (line)]] | wt | 67.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW 1088 (line)]] | alt | 87.9 | 0 | 1 | — | [[Sacubitril_Valsartan (drug)]] 5 µM 0.0647× (z -9.8) |
| [[A-427 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 94.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 59.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYK2]] | +0.60 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[MIB2]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[CCDC9]] | +0.54 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[AP3D1]] | +0.52 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[TMEM63B]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ASPSCR1]] | +0.50 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[NEURL4]] | +0.50 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[CIC]] | +0.49 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[SAFB2]] | +0.48 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[STK19]] | +0.48 | +0.46 / +0.39 | both halves | 6e-05 |  |
| [[OSBPL2]] | +0.47 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[GRIN2C]] | +0.47 | +0.32 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDHB]] | -0.46 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[ATXN7L3B]] | -0.45 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[FABP5]] | -0.45 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[WDCP]] | -0.44 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[UBE3D]] | -0.44 | -0.40 / -0.48 | both halves | 5e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[GLO1]] | -0.43 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[PTK2]] | -0.41 | -0.23 / -0.31 | both halves | 5e-04 | same gene group |
| [[EEF1E1]] | -0.40 | -0.32 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-13.8, -26.5); signed map (-10.2, 4.5). **Vector** length 89.0, 18.4% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.1 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.4 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.9 | -1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +0.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.6 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.6 | -5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.2 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Busulfan (drug)]] 5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mahogunin ring finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,616,493-4,690,974 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0544, RNF156 |
| Gene groups (HGNC) | Ring finger proteins; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O60291](https://www.uniprot.org/uniprotkb/O60291) (E3 ubiquitin-protein ligase MGRN1):

> E3 ubiquitin-protein ligase, which mediates ubiquitination of target proteins, such as MC1R, MC4R, smoothened (SMO) and TSG101. Catalytic component of the MMM ubiquitin ligase complex, a multiprotein complex that acts as a negative regulator of smoothened signaling pathway by mediating the ubiquitination and degradation of SMO in primary cilia. Catalytic component of a membrane-tethered ubiquitin ligase complex that acts as a negative regulator of melanocortin receptor signaling by mediating …

**Summary**, from NCBI Gene [23295](https://www.ncbi.nlm.nih.gov/gene/23295):

> Enables protein sequestering activity and ubiquitin-protein transferase activity. Involved in endosome to lysosome transport; negative regulation of adenylate cyclase-activating G protein-coupled receptor signaling pathway; and protein monoubiquitination. Located in early endosome; nucleus; and plasma membrane. Is active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20254) · Entrez [23295](https://www.ncbi.nlm.nih.gov/gene/23295) · UniProt [O60291](https://www.uniprot.org/uniprotkb/O60291) · Ensembl [ENSG00000102858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102858)

## Data

Gene col 2277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2277); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2277]; `tensor/DDL_lfc|DDL_z.npy` [2277]; `embed/gene_vectors.npy` [2277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2277 or target_col == 2277). Every well: [[MGRN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGRN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
