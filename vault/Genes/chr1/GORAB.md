---
symbol: "GORAB"
type: "gene"
col: 4181
ensembl_id: "ENSG00000120370"
name: "golgin, RAB6 interacting"
location: "1q24.2"
module: 12
arm: "+"
pooled_cpm: 23.43
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# GORAB

*golgin, RAB6 interacting* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.30× (z +36.2, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.446× (z -20.0, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX12]] (+0.73, fdr 7e-06), [[ZNF620]] (+0.72, fdr 7e-06), [[CLK4]] (+0.71, fdr 7e-06); moves opposite to [[NUTF2]] (-0.65, fdr 7e-06), [[ADAM15]] (-0.64, fdr 7e-06), [[SMARCD2]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.30×** | +36.2 | 0e+00 | 47/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.04×** | +27.5 | 0e+00 | 47/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.37×** | +21.5 | 0e+00 | 47/47 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.29×** | +11.0 | 4e-26 | 39/48 (HOP62, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +10.2 | 2e-22 | 32/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.20× | +4.5 | 7e-04 | 15/48 (A-172, A-427, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.25×** | +4.0 | 0.005 | 11/48 (A549, A-172, …) | rises with dose |  |
| [[Clotrimazole (drug)]] 5 µM |  | 1.14× | +3.2 | 0.12 | 1/48 (PANC-1) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.1 | 0.12 | 11/48 (A498, NCI-H2347, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4181.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.446×** | -20.0 | 0e+00 | 43/46 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.466×** | -13.5 | 3e-39 | 34/42 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.579×** | -9.3 | 3e-18 | 24/30 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.619×** | -8.5 | 3e-15 | 31/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -8.4 | 5e-15 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.627×** | -8.3 | 1e-14 | 32/46 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.604×** | -8.3 | 1e-14 | 26/35 (A-172, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -8.1 | 3e-14 | 28/46 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -7.7 | 9e-13 | 31/48 (A-427, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.653×** | -7.5 | 3e-12 | 29/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.716×** | -5.9 | 2e-07 | 28/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.724×** | -5.7 | 5e-07 | 24/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.761×** | -4.8 | 6e-05 | 21/48 (SW480, HOP62, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.612×** | -4.5 | 2e-04 | 15/29 (SNU-423, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.777×** | -4.5 | 3e-04 | 13/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -3.6 | 0.010 | 14/48 (SHP-77, H4, …) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.877× | -3.2 | 0.034 | 8/48 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.836× | -3.2 | 0.041 | 10/48 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.837× | -3.0 | 0.062 | 15/45 (A-427, BT-474, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.848× | -2.9 | 0.086 | 8/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.0 | 4 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +16.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -13.6) |
| [[A-172 (line)]] | wt | 45.4 | 4 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +27.4) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -16.1) |
| [[A498 (line)]] | wt | 40.5 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +24.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -14.2) |
| [[HS-578T (line)]] | alt | 33.1 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +19.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -15.4) |
| [[PANC-1 (line)]] | alt | 19.3 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +25.3) | [[Digitoxin (drug)]] 5 µM 0.245× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -10.5) |
| [[SW 900 (line)]] | alt | 53.8 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -11.7) |
| [[SW480 (line)]] | alt | 17.7 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -15.8) |
| [[A-427 (line)]] | wt | 19.6 | 3 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +9.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0986× (z -15.1) |
| [[A549 (line)]] | wt | 22.5 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +21.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -9.9) |
| [[HOP62 (line)]] | alt | 23.4 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +19.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.7) |
| [[Hs 766T (line)]] | wt | 41.7 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 23.6 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +18.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 16.7 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 40.1 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.0796× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 16.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +17.5) | — |
| [[J82 (line)]] | alt | 29.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +21.0) | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 18.7 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.159× (z -11.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 23.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 24.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 39.5 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 21.4 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -12.1) |
| [[RKO (line)]] | wt | 28.2 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +13.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -11.0) |
| [[BT-474 (line)]] | alt | 22.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.0921× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 17.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +20.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 17.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 12.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +13.9) | — |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.9) |
| [[SNU-423 (line)]] | alt | 27.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +19.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 22.9 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 4.72× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -15.5) |
| [[H4 (line)]] | wt | 26.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 12.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.158× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 18.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 20.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.3) |
| [[SW48 (line)]] | wt | 16.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +11.4) | — |
| [[KATO III (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.119× (z -10.2) |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX12]] | +0.73 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[ZNF620]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[CLK4]] | +0.71 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[ZNF23]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[ZNF140]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.70 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[PHAX]] | +0.69 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[TJAP1]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[METTL18]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[RP9]] | +0.68 | +0.76 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTF2]] | -0.65 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[ADAM15]] | -0.64 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[SMARCD2]] | -0.63 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[ARHGEF7]] | -0.63 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[PRDM10]] | -0.62 | -0.78 / -0.62 | both halves | 7e-06 |  |
| [[HACD3]] | -0.62 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[CD81]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[PIGN]] | -0.60 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[TAF4]] | -0.60 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[TMED4]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[SLC41A3]] | -0.59 | -0.65 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GORAB's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ILRUN]] | C | ILRUN's natural level weakens GORAB's drug response | ILRUN's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.05; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.4, 4.4); signed map (2.4, -22.2). **Vector** length 118, 31.4% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +13.9 | +27.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +13.2 | +36.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.6 | +21.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.5 | +10.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +1.4 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.8 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -7.0 | -7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -20.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.2 | -8.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.7 | -8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | golgin, RAB6 interacting |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:170,531,819-170,553,834 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11752, NTKL-BP1, GO; previously SCYL1BP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T7V8](https://www.uniprot.org/uniprotkb/Q5T7V8) (RAB6-interacting golgin):

> Plays a role in the organization and function of the Golgi apparatus. Involved in protein post-translational modification, particularly glycosylation of extracellular matrix proteins. Functions at the trans-Golgi by cooperating with SCYL1 to promote COPI coat assembly into discrete functional domains, supporting Golgi organization and trafficking.

**Summary**, from NCBI Gene [92344](https://www.ncbi.nlm.nih.gov/gene/92344):

> This gene encodes a member of the golgin family, a group of coiled-coil proteins localized to the Golgi. The encoded protein may function in the secretory pathway. The encoded protein, which also localizes to the cytoplasm, was identified by interactions with the N-terminal kinase-like protein, and thus it may function in mitosis. Mutations in this gene have been associated with geroderma osteodysplastica. Alternatively spliced transcript variants have been described. [provided by RefSeq, Mar …

**Accessions** — [HGNC:25676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25676) · Entrez [92344](https://www.ncbi.nlm.nih.gov/gene/92344) · UniProt [Q5T7V8](https://www.uniprot.org/uniprotkb/Q5T7V8) · Ensembl [ENSG00000120370](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120370)

## Data

Gene col 4181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4181); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4181]; `tensor/DDL_lfc|DDL_z.npy` [4181]; `embed/gene_vectors.npy` [4181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4181 or target_col == 4181). Every well: [[GORAB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GORAB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
