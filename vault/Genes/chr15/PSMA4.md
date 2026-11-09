---
symbol: "PSMA4"
type: "gene"
col: 475
ensembl_id: "ENSG00000041357"
name: "proteasome 20S subunit alpha 4"
location: "15q25.1"
module: 64
arm: "+"
pooled_cpm: 73.17
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PSMA4

*proteasome 20S subunit alpha 4* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.21× (z +10.5, q 5e-23, up in 41 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.53× (z +8.7, q 7e-16, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.0817×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB6]] (+0.74, fdr 7e-06), [[PSMD7]] (+0.71, fdr 7e-06), [[ALOX12P2-1]] (+0.71, fdr 7e-06); moves opposite to [[ARHGAP1]] (-0.55, fdr 1e-05), [[FUCA1]] (-0.54, fdr 2e-05), [[CRLS1]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.21×** | +10.5 | 5e-23 | 41/43 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.40×** | +10.3 | 2e-22 | 49/49 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.53×** | +8.7 | 7e-16 | 46/48 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.36×** | +8.0 | 1e-13 | 46/48 (NCI-H1573, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.08×** | +6.4 | 2e-08 | 34/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.02×** | +6.2 | 5e-08 | 43/48 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +5.3 | 1e-05 | 35/48 (NCI-H1573, A549, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.2 | 1e-05 | 37/47 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.66×** | +4.8 | 1e-04 | 39/48 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.67×** | +4.6 | 2e-04 | 37/48 (A549, NCI-H1573, …) | two highest doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.3 | 8e-04 | 40/48 (C32, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.50×** | +3.8 | 0.007 | 30/48 (COLO 205, H4, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.51×** | +3.7 | 0.009 | 31/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.065 | 25/48 (A-172, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 475.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.0817×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.538× | -3.0 | 0.81 | 32/49 (SW480, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 44.0 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.10× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 85.6 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.38× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 59.4 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.45× (z +11.7) | — |
| [[A-172 (line)]] | wt | 86.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 83.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 85.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.54× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[COLO 205 (line)]] | alt | 62.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.01× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 116 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.25× (z +8.8) | — |
| [[J82 (line)]] | alt | 72.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 52.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.99× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 40.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.21× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 61.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.44× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 75.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 50.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 75.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 39.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.66× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 62.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0817× (z -11.8) |
| [[H4 (line)]] | wt | 65.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 70.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 53.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 46.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 73.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 76.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 101 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB6]] | +0.74 | +0.82 / +0.68 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD7]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[ALOX12P2-1]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[PSMA1]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[ATP10D]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.63 | +0.70 / +0.50 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[NMT1]] | +0.62 | +0.65 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[GNGT1]] | +0.62 | +0.65 / +0.45 | both halves | 3e-05 | pathway: Beta-catenin independent WNT signaling |
| [[GCLM]] | +0.61 | +0.65 / +0.53 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[TYW3]] | +0.61 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[UBXN4]] | +0.61 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[HTATIP2]] | +0.61 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP1]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[FUCA1]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CRLS1]] | -0.53 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SPATA33]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SFXN2]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LINC01128]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MAN1B1]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[FHIP1B]] | -0.51 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[MTMR14]] | -0.51 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[FBXO31]] | -0.50 | -0.47 / -0.49 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[AP3S1]] | -0.49 | -0.49 / -0.49 | both halves | 2e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[RNASET2]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-6.9, 47.6); signed map (49.6, -8.8). **Vector** length 84.4, 32.4% of its response variance represented; |z| ≥ 3 in 701 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.3 | +8.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.2 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.9 | +8.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +4.0 | +4.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.9 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +1.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.5 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -4.0 | +6.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | +0.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.6 | -0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.5 | +1.7 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -1.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit alpha 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,540,405-78,552,417 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HC9, HsT17706 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 170 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P25789](https://www.uniprot.org/uniprotkb/P25789) (Proteasome subunit alpha type-4):

> Component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged …

**Summary**, from NCBI Gene [5685](https://www.ncbi.nlm.nih.gov/gene/5685):

> This gene encodes a core alpha subunit of the 20S proteosome, which is a highly ordered ring-shaped structure composed of four rings of 28 non-identical subunits. Proteasomes cleave peptides in an ATP- and ubiquitin-dependent manner. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:9533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9533) · Entrez [5685](https://www.ncbi.nlm.nih.gov/gene/5685) · UniProt [P25789](https://www.uniprot.org/uniprotkb/P25789) · Ensembl [ENSG00000041357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000041357)

## Data

Gene col 475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 475); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 475]; `tensor/DDL_lfc|DDL_z.npy` [475]; `embed/gene_vectors.npy` [475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 475 or target_col == 475). Every well: [[PSMA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
