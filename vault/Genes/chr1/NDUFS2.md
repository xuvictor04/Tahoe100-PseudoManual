---
symbol: "NDUFS2"
type: "gene"
col: 8201
ensembl_id: "ENSG00000158864"
name: "NADH:ubiquinone oxidoreductase core subunit S2"
location: "1q23.3"
module: 178
arm: "+"
pooled_cpm: 30.05
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# NDUFS2

*NADH:ubiquinone oxidoreductase core subunit S2* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.71× (z +8.6, q 4e-15, up in 33 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Medroxyprogesterone acetate (drug)]] 0.5 µM: 1.33× (z +4.5, q 8e-04, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -14.2, q 5e-43, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFV1]] (+0.64, fdr 1e-05), [[MRS2]] (+0.62, fdr 1e-05), [[TMEM183A]] (+0.62, fdr 1e-05); moves opposite to [[MAMLD1]] (-0.55, fdr 1e-05), [[AGO2]] (-0.52, fdr 3e-05), [[NFATC1]] (-0.52, fdr 2e-05).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +8.6 | 4e-15 | 33/43 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.0 | 5e-07 | 24/38 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | **1.33×** | +4.6 | 8e-04 | 23/45 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 8e-04 | 22/46 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +4.2 | 0.003 | 21/42 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.009 | 17/45 (NCI-H1792, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.063 | 14/48 (A-172, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8201.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -14.2 | 5e-43 | 39/47 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -8.6 | 2e-15 | 36/48 (MIA PaCa-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.611×** | -7.9 | 6e-13 | 38/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.622×** | -7.6 | 4e-12 | 40/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.645×** | -7.0 | 3e-10 | 33/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.706×** | -5.4 | 7e-06 | 29/48 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.716×** | -5.3 | 7e-06 | 29/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.719×** | -5.3 | 1e-05 | 25/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -5.0 | 4e-05 | 26/47 (BT-474, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -4.7 | 1e-04 | 20/48 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.749×** | -4.6 | 2e-04 | 22/47 (SW480, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.760×** | -4.2 | 0.001 | 20/46 (SNU-423, RKO, …) | top dose only |  |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.766×** | -4.1 | 0.002 | 17/47 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.797×** | -3.6 | 0.011 | 16/47 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.802×** | -3.5 | 0.015 | 12/47 (HS-578T, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.018 | 17/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 32.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -12.1) |
| [[C32 (line)]] | wt | 66.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -11.3) |
| [[J82 (line)]] | alt | 19.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.3) |
| [[PANC-1 (line)]] | alt | 28.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -11.9) |
| [[A-172 (line)]] | wt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.5) |
| [[A549 (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.181× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.0) |
| [[Hs 766T (line)]] | wt | 33.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.9) |
| [[LoVo (line)]] | wt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 93.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 78.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 30.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.2) |
| [[SHP-77 (line)]] | alt | 44.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -8.9) |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.0) |
| [[SW480 (line)]] | alt | 26.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.420× (z -8.6) |
| [[A-427 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFV1]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[MRS2]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TMEM183A]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[HARS2]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[NDUFB7]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[TMEM9]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TENT2]] | +0.60 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[METTL22]] | +0.60 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[ADH5]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[TRAPPC2]] | +0.59 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[TRAPPC11]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAMLD1]] | -0.55 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[AGO2]] | -0.52 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[NFATC1]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[STK10]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[KDSR]] | -0.51 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[LARP1B]] | -0.50 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[NOTCH2NLB]] | -0.50 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[LINC02798]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ACVR1C]] | -0.49 | -0.60 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.3, -12.2); signed map (-31.1, -14.5). **Vector** length 70.5, 13.1% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +0.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -14.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -7.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[9-ING-41 (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase core subunit S2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,197,104-161,214,723 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CI-49 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O75306](https://www.uniprot.org/uniprotkb/O75306) (NADH dehydrogenase):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Essential for the catalytic activity of complex I. Essential for the assembly of complex I (By similarity). Redox-sensitive, critical component of the oxygen-sensing pathway in the pulmonary vasculature which plays a key role in acute pulmonary oxygen-sensing and hypoxic pulmonary …

**Summary**, from NCBI Gene [4720](https://www.ncbi.nlm.nih.gov/gene/4720):

> The protein encoded by this gene is a core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I). Mammalian mitochondrial complex I is composed of at least 43 different subunits, 7 of which are encoded by the mitochondrial genome, and the rest are the products of nuclear genes. The iron-sulfur protein fraction of complex I is made up of 7 subunits, including this gene product. Complex I catalyzes the NADH oxidation with concomitant ubiquinone reduction and …

**Accessions** — [HGNC:7708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7708) · Entrez [4720](https://www.ncbi.nlm.nih.gov/gene/4720) · UniProt [O75306](https://www.uniprot.org/uniprotkb/O75306) · Ensembl [ENSG00000158864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158864)

## Data

Gene col 8201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8201); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8201]; `tensor/DDL_lfc|DDL_z.npy` [8201]; `embed/gene_vectors.npy` [8201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8201 or target_col == 8201). Every well: [[NDUFS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
