---
symbol: "EIF3L"
type: "gene"
col: 1874
ensembl_id: "ENSG00000100129"
name: "eukaryotic translation initiation factor 3 subunit L"
location: "22q13.1"
module: 43
arm: "+"
pooled_cpm: 105.78
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# EIF3L

*eukaryotic translation initiation factor 3 subunit L* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.77× (z +11.5, q 5e-28, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.72× (z +11.0, q 1e-25, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.776× (z -5.0, q 4e-04, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.522×; ⚠ cell-cycle shift, would explain all of this change); [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM in 1 line (SW 1088 0.113×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A6]] (+0.74, fdr 7e-06), [[EIF3H]] (+0.70, fdr 7e-06), [[EEF1G]] (+0.67, fdr 7e-06); moves opposite to [[PSME2]] (-0.57, fdr 1e-05), [[PBDC1]] (-0.56, fdr 8e-05), [[RBX1]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +11.5 | 5e-28 | 42/49 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +11.2 | 2e-26 | 36/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +11.0 | 1e-25 | 45/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +10.2 | 2e-22 | 45/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.56×** | +10.0 | 2e-21 | 45/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +9.8 | 1e-20 | 46/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +9.8 | 1e-20 | 2/50 (HepG2/C3A, H4) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +9.8 | 1e-20 | 45/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +8.7 | 3e-16 | 46/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +8.5 | 1e-15 | 39/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +8.3 | 6e-15 | 43/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.0 | 8e-11 | 33/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +6.6 | 1e-09 | 34/45 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.32×** | +5.7 | 6e-07 | 30/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.6 | 1e-06 | 34/45 (CFPAC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +4.2 | 1e-03 | 30/48 (PANC-1, C32, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.005 | 22/47 (SW480, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.6 | 0.008 | 22/48 (LoVo, KATO III, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.012 | 22/48 (A-427, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.024 | 21/47 (SK-MEL-2, KATO III, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.032 | 18/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.054 | 14/48 (NCI-H1792, J82, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1874.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.522×; ⚠ cell-cycle shift, would explain all of this change); [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM in 1 line (SW 1088 0.113×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.776×** | -5.0 | 4e-04 | 28/47 (A-427, C-33 A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.901× | -3.0 | 0.68 | 10/48 (A-427, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 136 | 9 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.47× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 105 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.97× (z +11.3) | — |
| [[LoVo (line)]] | wt | 139 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +15.5) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 61.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +16.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 137 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 86.3 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.00× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 90.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.91× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 84.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 51.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +11.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 93.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 95.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.8) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[SNU-1 (line)]] | wt | 164 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 94.3 | 0 | 1 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM 0.113× (z -8.6) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 93.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 171 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 167 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 122 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 116 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 156 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 186 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A6]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[EIF3H]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[EEF1G]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 | STRING 777 |
| [[QARS1]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | STRING 457 |
| [[EEF2]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 | STRING 736 |
| [[RPL3]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 642 |
| [[RPL14]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 457 |
| [[VTI1B]] | +0.62 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[PHB2]] | +0.62 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[EIF2S3]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 978 |
| [[CCNB1IP1]] | +0.61 | +0.68 / +0.37 | both halves | 7e-05 |  |
| [[HNRNPA1]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME2]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[PBDC1]] | -0.56 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[RBX1]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TOPORS]] | -0.53 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[KIAA1586]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ERVK3-1]] | -0.52 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[UNK]] | -0.52 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[TRIM5]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 | pathway: Interferon Signaling |
| [[IL27RA]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[IFI27]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 | pathway: Interferon Signaling |
| [[PLEKHA4]] | -0.50 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[BAZ1A]] | -0.50 | -0.43 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.364). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-29.8, -26.8); signed map (-55.4, -8.7). **Vector** length 99.4, 30.4% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +11.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +9.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +8.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | -0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.6 | +0.1 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.4 | +0.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.8 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.6 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.5 | +5.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,848,868-37,889,407 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC021, HSPC025, EIF3S11; previously EIF3S6IP, EIF3EIP |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 3 complex subunits |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y262](https://www.uniprot.org/uniprotkb/Q9Y262) (Eukaryotic translation initiation factor 3 subunit L):

> Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for disassembly …

**Summary**, from NCBI Gene [51386](https://www.ncbi.nlm.nih.gov/gene/51386):

> Enables RNA binding activity. Contributes to translation initiation factor activity. Involved in translational initiation and viral translational termination-reinitiation. Located in membrane. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18138) · Entrez [51386](https://www.ncbi.nlm.nih.gov/gene/51386) · UniProt [Q9Y262](https://www.uniprot.org/uniprotkb/Q9Y262) · Ensembl [ENSG00000100129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100129)

## Data

Gene col 1874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1874); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1874]; `tensor/DDL_lfc|DDL_z.npy` [1874]; `embed/gene_vectors.npy` [1874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1874 or target_col == 1874). Every well: [[EIF3L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
