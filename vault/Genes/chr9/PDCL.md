---
symbol: "PDCL"
type: "gene"
col: 5946
ensembl_id: "ENSG00000136940"
name: "phosducin like"
location: "9q33.2"
module: 69
arm: "+"
pooled_cpm: 23.24
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# PDCL

*phosducin like* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +18.1, q 0e+00, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.494× (z -6.8, q 5e-09, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKRN1]] (+0.64, fdr 1e-05), [[C1orf174]] (+0.62, fdr 1e-05), [[MACO1]] (+0.61, fdr 1e-05); moves opposite to [[ABCE1]] (-0.57, fdr 3e-05), [[TRIM44]] (-0.55, fdr 3e-05), [[ANAPC7]] (-0.55, fdr 5e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +18.1 | 0e+00 | 38/47 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +10.6 | 5e-24 | 40/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.64×** | +9.1 | 1e-17 | 31/48 (SW480, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +5.0 | 6e-05 | 19/47 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.33×** | +5.0 | 6e-05 | 23/45 (J82, HCT15, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 2e-04 | 19/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.30×** | +4.8 | 2e-04 | 19/48 (SW480, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.30×** | +4.7 | 2e-04 | 21/48 (RKO, C-33 A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.6 | 2e-04 | 20/48 (J82, H4, …) | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.5 | 4e-04 | 17/39 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.002 | 17/47 (HEC-1-A, SW480, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.1 | 0.002 | 2/48 (NCI-H2030, MIA PaCa-2) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.003 | 17/46 (NCI-H23, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.005 | 12/46 (BT-474, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.010 | 16/48 (RKO, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.032 | 15/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.035 | 11/48 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.494×** | -6.8 | 5e-09 | 31/48 (A-427, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.773×** | -6.7 | 5e-09 | 24/47 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.747×** | -5.4 | 1e-05 | 25/48 (SW1417, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.780×** | -4.6 | 6e-04 | 22/48 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.664×** | -4.0 | 0.008 | 17/47 (LOX-IMVI, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.821×** | -3.7 | 0.025 | 9/47 (A-172, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.3 | 0.085 | 16/47 (KATO III, HT-29, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.885× | -3.2 | 0.089 | 6/48 (HS-578T, Hs 766T, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.845× | -3.1 | 0.11 | 20/47 (HCT15, Hs 766T, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -3.1 | 0.11 | 15/48 (NCI-H2347, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 31.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +9.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -11.3) ⚠ cell-cycle shift, explains ~2% of this change |
| [[A-172 (line)]] | wt | 29.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.6) | — |
| [[A498 (line)]] | wt | 46.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.487× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 42.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +12.4) | — |
| [[COLO 205 (line)]] | alt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.0) |
| [[HCT15 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.2) |
| [[KATO III (line)]] | alt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 17.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0683× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.206× (z -8.8) |
| [[SNU-1 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -12.1) ⚠ cell-cycle shift, explains ~2% of this change |
| [[SW1417 (line)]] | alt | 28.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.4) | — |
| [[SW480 (line)]] | alt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.8) | — |
| [[A-427 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN1]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[C1orf174]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[MACO1]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[GTF3C5]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SCNM1]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ORMDL3]] | +0.59 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[MXD4]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[CPEB3]] | +0.57 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[KLHDC3]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TSEN34]] | +0.57 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SAP130]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[DEDD2]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCE1]] | -0.57 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[TRIM44]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[ANAPC7]] | -0.55 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[COA7]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[TMEM185B]] | -0.54 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[CEP83]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RRP15]] | -0.53 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[ZNF121]] | -0.53 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MRRF]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[DNAH14]] | -0.53 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[SFPQ]] | -0.52 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[SRFBP1]] | -0.52 | -0.51 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.378). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.6, -17.4); signed map (-23.9, 10.9). **Vector** length 84.0, 16.5% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +18.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.0 | +3.3 |
|  | [[NG25 (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.9 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.1 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -5.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | phosducin like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:122,798,389-122,828,588 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PhLP, DKFZp564M1863 |
| Reactome | 3 pathways, smallest: Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13371](https://www.uniprot.org/uniprotkb/Q13371) (Phosducin-like protein):

> Acts as a positive regulator of hedgehog signaling and regulates ciliary function.; [Isoform 1]: Functions as a co-chaperone for CCT in the assembly of heterotrimeric G protein complexes, facilitates the assembly of both Gbeta-Ggamma and RGS-Gbeta5 heterodimers.; [Isoform 2]: Acts as a negative regulator of heterotrimeric G proteins assembly by trapping the preloaded G beta subunits inside the CCT chaperonin.

**Summary**, from NCBI Gene [5082](https://www.ncbi.nlm.nih.gov/gene/5082):

> Phosducin-like protein is a putative modulator of heterotrimeric G proteins. The protein shares extensive amino acid sequence homology with phosducin, a phosphoprotein expressed in retina and pineal gland. Both phosducin-like protein and phosphoducin have been shown to regulate G-protein signaling by binding to the beta-gamma subunits of G proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8770) · Entrez [5082](https://www.ncbi.nlm.nih.gov/gene/5082) · UniProt [Q13371](https://www.uniprot.org/uniprotkb/Q13371) · Ensembl [ENSG00000136940](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136940)

## Data

Gene col 5946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5946); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5946]; `tensor/DDL_lfc|DDL_z.npy` [5946]; `embed/gene_vectors.npy` [5946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5946 or target_col == 5946). Every well: [[PDCL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
