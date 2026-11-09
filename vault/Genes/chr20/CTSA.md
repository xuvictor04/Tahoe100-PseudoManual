---
symbol: "CTSA"
type: "gene"
col: 750
ensembl_id: "ENSG00000064601"
name: "cathepsin A"
location: "20q13.12"
module: 122
arm: "+"
pooled_cpm: 62.68
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# CTSA

*cathepsin A* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.21× (z +10.8, q 1e-24, up in 41 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.35× (z +4.0, q 0.006, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.559× (z -7.6, q 1e-11, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRN]] (+0.78, fdr 7e-06), [[ATP6AP1]] (+0.73, fdr 7e-06), [[TPP1]] (+0.73, fdr 7e-06); moves opposite to [[TMA16]] (-0.52, fdr 1e-04), [[BRIX1]] (-0.50, fdr 4e-05), [[PMS1]] (-0.47, fdr 3e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +10.8 | 1e-24 | 41/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +9.9 | 1e-20 | 34/38 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.8 | 1e-06 | 28/41 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.9 | 1e-04 | 30/46 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.006 | 25/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.028 | 23/47 (RKO, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.057 | 23/47 (KATO III, SNU-423, …) | top dose only | position effect removed |
| [[4EGI-1 (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.090 | 18/46 (NCI-H460, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.18× | +3.2 | 0.094 | 15/47 (A498, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.17× | +3.0 | 0.15 | 21/48 (HEC-1-A, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.559×** | -7.6 | 1e-11 | 36/48 (HepG2/C3A, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -7.5 | 2e-11 | 31/46 (SW 900, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.606×** | -6.8 | 2e-09 | 39/47 (SNU-1, SW 900, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -6.2 | 7e-08 | 34/47 (COLO 205, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.717×** | -4.2 | 0.003 | 29/46 (C32, A-172, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.806×** | -4.2 | 0.003 | 24/47 (SW 900, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -4.1 | 0.004 | 26/47 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.764×** | -3.5 | 0.029 | 21/47 (C32, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.620×** | -3.4 | 0.040 | 23/47 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.783×** | -3.2 | 0.089 | 18/46 (SW1417, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 88.5 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.0) | [[Verteporfin (drug)]] 5 µM 0.382× (z -9.1) |
| [[C32 (line)]] | wt | 61.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 87.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -8.8) |
| [[A-427 (line)]] | wt | 41.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 31.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 73.6 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.06× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -13.3) |
| [[A498 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +9.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 54.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.333× (z -8.9) |
| [[COLO 205 (line)]] | alt | 100 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.298× (z -8.7) |
| [[H4 (line)]] | wt | 44.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 60.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.274× (z -9.6) |
| [[Hs 766T (line)]] | wt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.6) | — |
| [[KATO III (line)]] | alt | 57.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 28.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 60.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 68.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 67.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -8.6) |
| [[PANC-1 (line)]] | alt | 41.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +10.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 51.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 38.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.147× (z -11.3) |
| [[SW480 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRN]] | +0.78 | +0.86 / +0.70 | both halves | 7e-06 | STRING 539 |
| [[ATP6AP1]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TPP1]] | +0.73 | +0.68 / +0.74 | both halves | 7e-06 | STRING 623 |
| [[NEU1]] | +0.67 | +0.61 / +0.58 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 999 |
| [[GLMP]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SPNS1]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[CTSD]] | +0.65 | +0.70 / +0.56 | both halves | 1e-05 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 824 |
| [[GNS]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 | pathway: Diseases of metabolism; STRING 512 |
| [[MCOLN1]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 | STRING 575 |
| [[PSAP]] | +0.61 | +0.71 / +0.46 | both halves | 3e-05 | pathway: Glycosphingolipid catabolism; STRING 523 |
| [[LRPAP1]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LAMP1]] | +0.60 | +0.69 / +0.45 | both halves | 3e-05 | STRING 601 |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMA16]] | -0.52 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[BRIX1]] | -0.50 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[PMS1]] | -0.47 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TCERG1]] | -0.47 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[RIOX2]] | -0.46 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[TCHP]] | -0.46 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ICE2]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[HSF2BP]] | -0.45 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[TADA2A]] | -0.45 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[FBXO45]] | -0.45 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[KAT14]] | -0.45 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[ASAH2B]] | -0.44 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-21.3, -20.5); signed map (-24.5, -36.0). **Vector** length 107, 30.0% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.2 | +4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | +2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.1 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.2 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.1 | -6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.6 | -4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.5 | -7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,890,144-45,898,949 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GSL, PPGB |
| Gene groups (HGNC) | Cathepsins |
| Reactome | 19 pathways, smallest: Defective NEU1 causes sialidosis; Diseases associated with N-glycosylation of proteins; Glycosphingolipid catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P10619](https://www.uniprot.org/uniprotkb/P10619) (Lysosomal protective protein):

> Protective protein appears to be essential for both the activity of beta-galactosidase and neuraminidase, it associates with these enzymes and exerts a protective function necessary for their stability and activity. Also functions as an activator of the sialidase NEU1. This protein is also a carboxypeptidase and can deamidate tachykinins.

**Summary**, from NCBI Gene [5476](https://www.ncbi.nlm.nih.gov/gene/5476):

> This gene encodes a member of the peptidase S10 family of serine carboxypeptidases. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate two chains that comprise the heterodimeric active enzyme. This enzyme possesses deamidase, esterase and carboxypeptidase activities and acts as a scaffold in the lysosomal multienzyme complex. Mutations in this gene are associated with galactosialidosis. …

**Accessions** — [HGNC:9251](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9251) · Entrez [5476](https://www.ncbi.nlm.nih.gov/gene/5476) · UniProt [P10619](https://www.uniprot.org/uniprotkb/P10619) · Ensembl [ENSG00000064601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064601)

## Data

Gene col 750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 750); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 750]; `tensor/DDL_lfc|DDL_z.npy` [750]; `embed/gene_vectors.npy` [750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 750 or target_col == 750). Every well: [[CTSA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
