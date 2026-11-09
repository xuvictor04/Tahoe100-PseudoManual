---
symbol: "CHURC1"
type: "gene"
col: 15093
ensembl_id: "ENSG00000258289"
name: "churchill domain containing 1"
location: "14q23.3"
module: 28
arm: "+"
pooled_cpm: 63.55
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CHURC1

*churchill domain containing 1* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.86× (z +10.8, q 1e-24, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.42× (z +6.2, q 1e-07, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.660× (z -10.3, q 3e-22, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OCIAD1]] (+0.75, fdr 7e-06), [[MRPS33]] (+0.73, fdr 7e-06), [[COPS5]] (+0.70, fdr 7e-06); moves opposite to [[SMG1P2]] (-0.70, fdr 7e-06), [[TBC1D24]] (-0.64, fdr 7e-06), [[VAV2]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +10.8 | 1e-24 | 44/49 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.3 | 2e-14 | 35/44 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +6.2 | 1e-07 | 33/47 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +5.6 | 3e-06 | 34/48 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.1 | 4e-05 | 31/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.8 | 1e-04 | 25/45 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +3.9 | 0.009 | 24/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.7 | 0.014 | 19/48 (NCI-H1573, SW48, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.014 | 25/48 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.16× | +3.7 | 0.015 | 20/47 (NCI-H2030, NCI-H23, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.027 | 14/48 (SW48, NCI-H2030, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.043 | 16/47 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15093.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -10.3 | 3e-22 | 37/49 (Panc 03.27, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.693×** | -6.4 | 3e-08 | 32/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -6.4 | 3e-08 | 36/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.698×** | -6.3 | 4e-08 | 32/48 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.753×** | -5.0 | 7e-05 | 32/48 (A549, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.767×** | -4.6 | 3e-04 | 26/48 (SW48, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.788×** | -4.2 | 0.002 | 23/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.798×** | -4.0 | 0.005 | 27/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | **0.799×** | -3.8 | 0.009 | 25/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.811×** | -3.5 | 0.030 | 20/48 (SW480, LoVo, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.822×** | -3.4 | 0.030 | 22/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 80.3 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 84.9 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +12.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 163 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.0) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -19.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 66.8 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.418× (z -11.3) |
| [[A-172 (line)]] | wt | 35.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.7) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 60.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 42.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 60.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -9.9) |
| [[PANC-1 (line)]] | alt | 50.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.8) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[A-427 (line)]] | wt | 62.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.6) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[CHP-212 (line)]] | wt | 47.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -9.6) |
| [[LoVo (line)]] | wt | 61.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 64.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.6) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[Panc 03.27 (line)]] | alt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.3) |
| [[A498 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCIAD1]] | +0.75 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[MRPS33]] | +0.73 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[COPS5]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ZNF780A]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.69 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.68 | +0.82 / +0.58 | both halves | 7e-06 |  |
| [[VPS72]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LARP7]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MRPL47]] | +0.67 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[AIMP1]] | +0.67 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P2]] | -0.70 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[TBC1D24]] | -0.64 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[VAV2]] | -0.63 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[KLHL25]] | -0.63 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[TENT4A]] | -0.62 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.61 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[CHAF1B]] | -0.59 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[POC1A]] | -0.59 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[INPP5A]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[PTDSS1]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.7, 5.7); signed map (5.7, -23.2). **Vector** length 109, 29.8% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.8 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +8.1 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +7.0 | +3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -0.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -10.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | -5.2 | -3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -3.4 | -5.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | churchill domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:64,914,361-64,944,591 (+) |
| Ensembl biotype | protein_coding |
| Also known as | My015, FLJ33064; previously C14orf52 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUH1](https://www.uniprot.org/uniprotkb/Q8WUH1) (Protein Churchill):

> Transcriptional activator that mediates FGF signaling during neural development (By similarity). Plays a role in the regulation of cell movement (By similarity).; [Isoform 4]: Does not bind DNA by itself.

**Summary**, from NCBI Gene [91612](https://www.ncbi.nlm.nih.gov/gene/91612):

> Predicted to enable zinc ion binding activity. Predicted to be involved in fibroblast growth factor receptor signaling pathway. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20099) · Entrez [91612](https://www.ncbi.nlm.nih.gov/gene/91612) · UniProt [Q8WUH1](https://www.uniprot.org/uniprotkb/Q8WUH1) · Ensembl [ENSG00000258289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258289)

## Data

Gene col 15093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15093); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15093]; `tensor/DDL_lfc|DDL_z.npy` [15093]; `embed/gene_vectors.npy` [15093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15093 or target_col == 15093). Every well: [[CHURC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHURC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
