---
symbol: "ZNF34"
type: "gene"
col: 12194
ensembl_id: "ENSG00000196378"
name: "zinc finger protein 34"
location: "8q24.3"
module: 47
arm: "+"
pooled_cpm: 5.03
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# ZNF34

*zinc finger protein 34* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.71× (z +26.6, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.735× (z -3.8, q 0.089, down in 13 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.0573×, A549 0.0802×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.0799×; ⚠ toxic; transcription drop); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0791×); [[Rosiglitazone (drug)]] 5 µM in 1 line (NCI-H2347 0.0784×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H460 0.0982×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMP25]] (+0.76, fdr 7e-06), [[ZNF543]] (+0.70, fdr 1e-05), [[C3orf20]] (+0.68, fdr 1e-05); moves opposite to [[STRN]] (-0.62, fdr 3e-05), [[NENF]] (-0.60, fdr 2e-05), [[SLC25A27]] (-0.58, fdr 1e-04).
> It is in [[Module 047]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.71×** | +26.6 | 0e+00 | 38/40 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +15.8 | 0e+00 | 38/41 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.35×** | +14.7 | 0e+00 | 32/39 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.93×** | +7.9 | 3e-13 | 24/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +7.9 | 4e-13 | 22/45 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +7.9 | 4e-13 | 3/9 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +7.4 | 1e-11 | 22/43 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.11×** | +7.2 | 5e-11 | 24/41 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.91×** | +6.8 | 8e-10 | 20/36 (LOX-IMVI, A498, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.75×** | +6.8 | 8e-10 | 22/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +6.3 | 2e-08 | 17/45 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.67×** | +6.2 | 3e-08 | 8/26 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.63×** | +5.7 | 7e-07 | 9/32 (HT-29, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.5 | 1e-06 | 15/44 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **2.21×** | +5.0 | 2e-05 | 8/39 (LOX-IMVI, A549, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +4.7 | 1e-04 | 14/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.07×** | +4.6 | 1e-04 | 7/38 (LOX-IMVI, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +4.5 | 2e-04 | 9/43 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +4.4 | 4e-04 | 13/39 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +4.2 | 7e-04 | 9/38 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.005 | 4/45 (HCT15, CHP-212, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12194.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.0573×, A549 0.0802×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.0799×; ⚠ toxic; transcription drop); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0791×); [[Rosiglitazone (drug)]] 5 µM in 1 line (NCI-H2347 0.0784×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H460 0.0982×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.735×** | -3.8 | 0.089 | 13/45 (PANC-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Fumaric acid (drug)]] 5 µM |  | 0.757× | -3.3 | 0.27 | 4/45 (RKO, J82, …) | top dose only | plate-row cell shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.780× | -3.1 | 0.31 | 16/37 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.783× | -3.0 | 0.31 | 10/45 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 10.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +12.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0573× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 2.54 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +14.5) | [[Pimozide (drug)]] 0.05 µM 0.0982× (z -8.9) |
| [[C32 (line)]] | wt | 6.96 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +14.5) | — |
| [[KATO III (line)]] | alt | 3.77 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0791× (z -8.6) |
| [[LoVo (line)]] | wt | 4.86 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 3.17 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0791× (z -9.6) |
| [[A498 (line)]] | wt | 5.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +13.0) | — |
| [[A549 (line)]] | wt | 8.90 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0802× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 4.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 9.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 4.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 2.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 3.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 8.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0799× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 5.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 6.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 5.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 4.32 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.0807× (z -8.8) |
| [[SW1417 (line)]] | alt | 5.18 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.100× (z -8.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 4.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +11.1) | — |
| [[A-172 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP25]] | +0.76 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.70 | +0.74 / +0.55 | both halves | 1e-05 | same gene group |
| [[C3orf20]] | +0.68 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[KPTN]] | +0.67 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[SH2D4B]] | +0.67 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[CYB5D1]] | +0.67 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[PPIEL]] | +0.66 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[LINC02236]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[GRIK5]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[CELSR3]] | +0.64 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | +0.63 | +0.67 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRN]] | -0.62 | -0.69 / -0.43 | both halves | 3e-05 |  |
| [[NENF]] | -0.60 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[SLC25A27]] | -0.58 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[SNX1]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[FBXO3]] | -0.56 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[FAM118A]] | -0.56 | -0.67 / -0.26 | both halves | 4e-04 |  |
| [[CBFA2T2]] | -0.55 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[SEC11A]] | -0.55 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[STK38]] | -0.54 | -0.57 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.8, -10.6); signed map (20.7, 11.1). **Vector** length 67.5, 10.4% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +26.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +6.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,772,224-144,787,348 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX32 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZ26](https://www.uniprot.org/uniprotkb/Q8IZ26) (Zinc finger protein 34):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [80778](https://www.ncbi.nlm.nih.gov/gene/80778):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13098) · Entrez [80778](https://www.ncbi.nlm.nih.gov/gene/80778) · UniProt [Q8IZ26](https://www.uniprot.org/uniprotkb/Q8IZ26) · Ensembl [ENSG00000196378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196378)

## Data

Gene col 12194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12194); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12194]; `tensor/DDL_lfc|DDL_z.npy` [12194]; `embed/gene_vectors.npy` [12194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12194 or target_col == 12194). Every well: [[ZNF34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
