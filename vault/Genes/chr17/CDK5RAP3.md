---
symbol: "CDK5RAP3"
type: "gene"
col: 2950
ensembl_id: "ENSG00000108465"
name: "CDK5 regulatory subunit associated protein 3"
location: "17q21.32"
module: 157
arm: "+"
pooled_cpm: 34.85
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# CDK5RAP3

*CDK5 regulatory subunit associated protein 3* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.17× (z +10.2, q 1e-21, up in 39 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.59× (z +4.3, q 0.002, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.633× (z -8.6, q 7e-15, down in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.537× (z -7.9, q 8e-13, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LENG8]] (+0.77, fdr 7e-06), [[CCNL2]] (+0.67, fdr 1e-05), [[CCDC183]] (+0.64, fdr 1e-05); moves opposite to [[MPLKIP]] (-0.53, fdr 4e-05), [[MRPL36]] (-0.53, fdr 3e-05), [[GSPT2]] (-0.49, fdr 7e-05).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +10.2 | 1e-21 | 39/45 (HEC-1-A, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +9.1 | 3e-17 | 37/42 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +9.0 | 6e-17 | 34/39 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +6.3 | 3e-08 | 5/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +4.3 | 0.002 | 32/47 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 0.002 | 26/46 (MIA PaCa-2, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.021 | 18/48 (KATO III, A549, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +3.3 | 0.079 | 18/47 (NCI-H460, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.2 | 0.088 | 13/39 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.12 | 13/48 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.26× | +3.0 | 0.13 | 12/47 (hTERT-HPNE, NCI-H2030, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.633×** | -8.6 | 7e-15 | 37/48 (H4, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.537×** | -7.9 | 8e-13 | 36/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.612×** | -6.5 | 2e-08 | 42/48 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.673×** | -5.2 | 2e-05 | 35/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.673×** | -5.2 | 2e-05 | 29/48 (NCI-H661, SW 900, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -5.2 | 2e-05 | 36/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -5.1 | 3e-05 | 27/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.692×** | -4.9 | 8e-05 | 37/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.697×** | -4.8 | 1e-04 | 26/47 (RKO, COLO 205, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.702×** | -4.7 | 2e-04 | 23/48 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.711×** | -4.5 | 3e-04 | 27/48 (SNU-423, SW480, …) | two highest doses | composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.743×** | -3.7 | 0.009 | 24/47 (RKO, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.751×** | -3.6 | 0.014 | 24/48 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 31.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 44.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.85× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 22.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.50× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 37.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 27.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +8.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 15.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.89× (z +9.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 71.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0770× (z -19.1) |
| [[Panc 03.27 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +8.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 49.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.392× (z -8.9) |
| [[RKO (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 36.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.254× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LENG8]] | +0.77 | +0.71 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CCNL2]] | +0.67 | +0.57 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[CCDC183]] | +0.64 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ANAPC2]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.62 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[ABCA2]] | +0.62 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[AKT2]] | +0.61 | +0.46 / +0.73 | both halves | 3e-05 |  |
| [[MAN1B1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SKIC2]] | +0.60 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SBF1]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[GANAB]] | +0.59 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[LMNTD2]] | +0.59 | +0.53 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPLKIP]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[MRPL36]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[GSPT2]] | -0.49 | -0.38 / -0.52 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.2, -24.7); signed map (-28.3, -2.1). **Vector** length 102, 24.6% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +9.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.3 | +3.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.7 | +1.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +2.7 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -7.9 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.6 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.0 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -1.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.6 | -2.1 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | CDK5 regulatory subunit associated protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,967,810-47,981,781 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MST016, FLJ13660, C53, IC53, HSF-27, OK/SW-cl.114, LZAP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JB5](https://www.uniprot.org/uniprotkb/Q96JB5) (CDK5 regulatory subunit-associated protein 3):

> Substrate adapter of E3 ligase complexes mediating ufmylation, the covalent attachment of the ubiquitin-like modifier UFM1 to substrate proteins, and which is involved in various processes, such as ribosome recycling and reticulophagy (also called ER-phagy). As part of the UREL complex, plays a key role in ribosome recycling by promoting mono-ufmylation of RPL26/uL24 subunit of the 60S ribosome. Ufmylation of RPL26/uL24 occurs on free 60S ribosomes following ribosome dissociation: it weakens …

**Summary**, from NCBI Gene [80279](https://www.ncbi.nlm.nih.gov/gene/80279):

> This gene encodes a protein that has been reported to function in signaling pathways governing transcriptional regulation and cell cycle progression. It may play a role in tumorigenesis and metastasis. A pseudogene of this gene is located on the long arm of chromosome 20. Alternative splicing results in multiple transcript variants that encode different isoforms. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:18673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18673) · Entrez [80279](https://www.ncbi.nlm.nih.gov/gene/80279) · UniProt [Q96JB5](https://www.uniprot.org/uniprotkb/Q96JB5) · Ensembl [ENSG00000108465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108465)

## Data

Gene col 2950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2950); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2950]; `tensor/DDL_lfc|DDL_z.npy` [2950]; `embed/gene_vectors.npy` [2950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2950 or target_col == 2950). Every well: [[CDK5RAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK5RAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
