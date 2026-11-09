---
symbol: "EMD"
type: "gene"
col: 2217
ensembl_id: "ENSG00000102119"
name: "emerin"
location: "Xq28"
module: 7
arm: "+"
pooled_cpm: 27.3
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# EMD

*emerin* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.80× (z +12.7, q 6e-34, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.66× (z +6.2, q 3e-08, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 0.05 µM: 0.649× (z -5.0, q 3e-04, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF1A2]] (+0.60, fdr 2e-05), [[RELA]] (+0.57, fdr 1e-05), [[FLII]] (+0.57, fdr 2e-05); moves opposite to [[ORC2]] (-0.55, fdr 2e-05), [[IL9RP3]] (-0.54, fdr 1e-04), [[AGAP4]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.80×** | +12.7 | 6e-34 | 41/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +11.9 | 2e-30 | 30/33 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.90×** | +7.6 | 6e-12 | 37/48 (AsPC-1, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +7.5 | 7e-12 | 32/38 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.49×** | +7.0 | 3e-10 | 30/47 (AsPC-1, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.74×** | +6.8 | 8e-10 | 32/45 (SW 900, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +6.2 | 3e-08 | 36/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.025 | 20/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.027 | 15/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.027 | 16/48 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.4 | 0.036 | 16/43 (NCI-H2030, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.31×** | +3.4 | 0.036 | 22/47 (SW1417, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.32×** | +3.3 | 0.040 | 21/47 (BT-474, NCI-H1573, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.051 | 21/47 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.080 | 13/44 (A549, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.090 | 17/47 (C-33 A, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2217.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **0.649×** | -5.0 | 3e-04 | 32/47 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.504×** | -4.4 | 0.003 | 26/48 (Hs 766T, NCI-H23, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **0.732×** | -3.8 | 0.025 | 22/47 (SHP-77, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.679× | -3.3 | 0.12 | 23/45 (HCT15, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 27.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 27.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +14.7) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[HOP62 (line)]] | alt | 22.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +11.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +10.0) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.283× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 32.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 46.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 19.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0932× (z -8.7) |
| [[KATO III (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.30× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.111× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.5) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[SW1417 (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.9) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[A-427 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1A2]] | +0.60 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[RELA]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[FLII]] | +0.57 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[GZF1]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[GRINA]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CREB3]] | +0.54 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[TAF9]] | +0.53 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MBD6]] | +0.53 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[DMXL1]] | +0.53 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[TPPP]] | +0.53 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[NUDT16]] | +0.53 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[DNAJB2]] | +0.52 | +0.59 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORC2]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[IL9RP3]] | -0.54 | -0.34 / -0.62 | both halves | 1e-04 |  |
| [[AGAP4]] | -0.51 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[PARGP1]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[SNRPD1]] | -0.49 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[INTS9]] | -0.49 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[SNRPB]] | -0.48 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[SNRPF]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[LINC02976]] | -0.47 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[HIRA]] | -0.47 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[LINC00106]] | -0.47 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[TYW1]] | -0.46 | -0.56 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.114). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-33.2, -17.4); signed map (8.2, -9.8). **Vector** length 81.9, 18.7% of its response variance represented; |z| ≥ 3 in 722 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.8 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.7 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | +3.0 | +6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | +0.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -3.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | emerin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,379,273-154,381,574 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STA, LEMD5 |
| Gene groups (HGNC) | LEM domain containing |
| Reactome | 20 pathways, smallest: Depolymerization of the Nuclear Lamina; Initiation of Nuclear Envelope (NE) Reformation; Insertion of tail-anchored proteins into the endoplasmic reticulum membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P50402](https://www.uniprot.org/uniprotkb/P50402) (Emerin):

> Stabilizes and promotes the formation of a nuclear actin cortical network. Stimulates actin polymerization in vitro by binding and stabilizing the pointed end of growing filaments. Inhibits beta-catenin activity by preventing its accumulation in the nucleus. Acts by influencing the nuclear accumulation of beta-catenin through a CRM1-dependent export pathway. Links centrosomes to the nuclear envelope via a microtubule association. Required for proper localization of non-farnesylated …

**Summary**, from NCBI Gene [2010](https://www.ncbi.nlm.nih.gov/gene/2010):

> Emerin is a serine-rich nuclear membrane protein and a member of the nuclear lamina-associated protein family. It mediates membrane anchorage to the cytoskeleton. Dreifuss-Emery muscular dystrophy is an X-linked inherited degenerative myopathy resulting from mutation in the emerin gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3331) · Entrez [2010](https://www.ncbi.nlm.nih.gov/gene/2010) · UniProt [P50402](https://www.uniprot.org/uniprotkb/P50402) · Ensembl [ENSG00000102119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102119)

## Data

Gene col 2217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2217); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2217]; `tensor/DDL_lfc|DDL_z.npy` [2217]; `embed/gene_vectors.npy` [2217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2217 or target_col == 2217). Every well: [[EMD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
