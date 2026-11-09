---
symbol: "DENND10"
type: "gene"
col: 4147
ensembl_id: "ENSG00000119979"
name: "DENN domain containing 10"
location: "10q26.11"
module: 15
arm: "+"
pooled_cpm: 12.53
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DENND10

*DENN domain containing 10* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +9.7, q 2e-19, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.626× (z -9.2, q 3e-17, down in 29 of 45 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.552× (z -7.9, q 7e-13, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF250]] (+0.73, fdr 7e-06), [[APTR]] (+0.68, fdr 7e-06), [[MFSD8]] (+0.67, fdr 7e-06); moves opposite to [[PPP1R10]] (-0.60, fdr 1e-05), [[SRSF3]] (-0.56, fdr 2e-05), [[ATP7A]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +9.7 | 2e-19 | 30/45 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +6.0 | 4e-07 | 28/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +4.9 | 1e-04 | 19/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.9 | 2e-04 | 13/23 (NCI-H2347, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +4.7 | 4e-04 | 15/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +4.5 | 7e-04 | 19/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.004 | 12/44 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.0 | 0.004 | 14/40 (HT-29, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.004 | 10/48 (SW480, LoVo, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.004 | 6/47 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.052 | 8/47 (HepG2/C3A, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.065 | 10/47 (SNU-1, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 1.17× | +3.2 | 0.068 | 14/48 (SNU-423, J82, …) | rises with dose | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.073 | 12/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.1 | 0.084 | 8/45 (A-427, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.626×** | -9.2 | 3e-17 | 29/45 (HepG2/C3A, NCI-H23, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.552×** | -7.9 | 7e-13 | 31/46 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.575×** | -7.7 | 3e-12 | 31/47 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -6.6 | 7e-09 | 26/47 (NCI-H1573, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.448×** | -5.8 | 7e-07 | 24/48 (Hs 766T, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.674×** | -5.5 | 4e-06 | 21/45 (HepG2/C3A, PANC-1, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.693×** | -5.1 | 3e-05 | 22/45 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -4.7 | 2e-04 | 19/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.522×** | -4.7 | 2e-04 | 13/43 (A-172, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.753×** | -3.9 | 0.005 | 12/47 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.763×** | -3.7 | 0.010 | 18/46 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.789×** | -3.2 | 0.076 | 14/45 (BT-474, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 53.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -13.0) |
| [[A-172 (line)]] | wt | 23.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.325× (z -9.0) |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -9.4) |
| [[A498 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.246× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[BT-474 (line)]] | alt | 5.53 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0843× (z -8.8) |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 1 | — | [[ERK5-IN-2 (drug)]] 0.5 µM 0.0657× (z -9.7) |
| [[HS-578T (line)]] | alt | 5.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0641× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 8.65 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 8.05 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -11.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 17.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -9.4) |
| [[SW48 (line)]] | wt | 14.8 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0756× (z -9.7) |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF250]] | +0.73 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[APTR]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[MFSD8]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[MIR762HG]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[CCZ1B]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[SLC35D2]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MTFMT]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CCT6P3-1]] | +0.64 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[TRPC4AP]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CCZ1]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZNF398]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CNIH4]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R10]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ATP7A]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[FOS]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[SGMS2]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[THOC6]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[HUWE1]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[YWHAE]] | -0.53 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CEP41]] | -0.52 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[CELSR3]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.3, 22.3); signed map (-36.6, 1.1). **Vector** length 68.2, 11.6% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +6.0 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.4 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +4.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.9 | -9.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -4.7 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.9 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +1.0 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:119,104,086-119,137,984 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM45A |
| Gene groups (HGNC) | DENN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCE6](https://www.uniprot.org/uniprotkb/Q8TCE6) (DENN domain-containing protein 10):

> Guanine nucleotide exchange factor (GEF) regulating homeostasis of late endocytic pathway, including endosomal positioning, maturation and secretion, possibly through activating Rab proteins such as RAB27A and RAB27B. Promotes the exchange of GDP to GTP, converting inactive GDP-bound RAB27A and RAB27B into their active GTP-bound form.

**Summary**, from NCBI Gene [404636](https://www.ncbi.nlm.nih.gov/gene/404636):

> Enables guanyl-nucleotide exchange factor activity and small GTPase binding activity. Involved in endosome transport via multivesicular body sorting pathway; protein transport; and regulation of early endosome to late endosome transport. Located in late endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31793](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31793) · Entrez [404636](https://www.ncbi.nlm.nih.gov/gene/404636) · UniProt [Q8TCE6](https://www.uniprot.org/uniprotkb/Q8TCE6) · Ensembl [ENSG00000119979](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119979)

## Data

Gene col 4147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4147); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4147]; `tensor/DDL_lfc|DDL_z.npy` [4147]; `embed/gene_vectors.npy` [4147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4147 or target_col == 4147). Every well: [[DENND10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
