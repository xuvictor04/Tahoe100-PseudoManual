---
symbol: "LEO1"
type: "gene"
col: 9316
ensembl_id: "ENSG00000166477"
name: "LEO1 component of Paf1/RNA polymerase II complex"
location: "15q21.2"
module: 12
arm: "+"
pooled_cpm: 63.03
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# LEO1

*LEO1 component of Paf1/RNA polymerase II complex* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.05 µM: 1.50× (z +4.6, q 0.002, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.523× (z -7.6, q 2e-11, down in 34 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.723× (z -3.9, q 0.012, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (C32 0.163×, CFPAC-1 0.281×, SNU-1 0.139×, LS 180 0.270×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 6 lines (SNU-1 0.120×, CFPAC-1 0.313×, A-172 0.279×, AN3 CA 0.108×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.145×, C-33 A 0.196×; ⚠ toxic; transcription drop); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.145×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.281×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TARS2]] (+0.77, fdr 7e-06), [[MRPL46]] (+0.75, fdr 1e-05), [[RBMX2]] (+0.74, fdr 7e-06); moves opposite to [[MOB1A]] (-0.65, fdr 3e-05), [[DHFR]] (-0.65, fdr 2e-04), [[GNG12]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.6 | 0.002 | 36/47 (SW480, HEC-1-A, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.5 | 0.002 | 33/48 (NCI-H1573, HEC-1-A, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.44×** | +4.4 | 0.002 | 30/48 (HT-29, SW480, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +4.2 | 0.003 | 33/48 (HEC-1-A, NCI-H1573, …) | all doses, flat | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.78×** | +3.7 | 0.029 | 32/48 (KATO III, NCI-H1573, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.66× | +3.2 | 0.12 | 27/47 (C32, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 1.30× | +3.1 | 0.18 | 25/48 (HEC-1-A, SW480, …) | all doses, flat | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9316.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (C32 0.163×, CFPAC-1 0.281×, SNU-1 0.139×, LS 180 0.270×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 6 lines (SNU-1 0.120×, CFPAC-1 0.313×, A-172 0.279×, AN3 CA 0.108×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.145×, C-33 A 0.196×; ⚠ toxic; transcription drop); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.145×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.281×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -7.6 | 2e-11 | 34/41 (NCI-H1573, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.560×** | -7.0 | 5e-10 | 35/48 (C32, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.537×** | -7.0 | 5e-10 | 35/45 (SNU-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.723×** | -3.9 | 0.012 | 27/48 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -3.5 | 0.055 | 27/49 (LOX-IMVI, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.764× | -3.3 | 0.11 | 23/48 (H4, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 83.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -11.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 67.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.281× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 77.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -12.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 48.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 97.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -10.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 70.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -10.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 77.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -11.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 55.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 71.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 60.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -8.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 60.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 79.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 60.8 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.145× (z -11.6) |
| [[PANC-1 (line)]] | alt | 70.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 85.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 61.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARS2]] | +0.77 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.75 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | +0.74 | +0.62 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RNF113A]] | +0.73 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[C1orf35]] | +0.72 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[GADD45GIP1]] | +0.71 | +0.39 / +0.76 | both halves | 6e-05 |  |
| [[RP9]] | +0.71 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.71 | +0.50 / +0.73 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MPHOSPH10]] | +0.70 | +0.62 / +0.67 | both halves | 7e-06 | STRING 604 |
| [[NKAP]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[PET117]] | +0.68 | +0.35 / +0.75 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.65 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[DHFR]] | -0.65 | -0.32 / -0.70 | both halves | 2e-04 |  |
| [[GNG12]] | -0.62 | -0.41 / -0.67 | both halves | 4e-05 | pathway: Signaling by WNT |
| [[STMP1]] | -0.61 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[FGD5-AS1]] | -0.61 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[UBE2V1]] | -0.61 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[CERS2]] | -0.60 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MMGT1]] | -0.60 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[CTSZ]] | -0.60 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[SSU72]] | -0.59 | -0.32 / -0.66 | both halves | 2e-04 |  |
| [[CTTN]] | -0.59 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[SELENON]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.9, -10.6); signed map (-14.4, -7.5). **Vector** length 124, 41.0% of its response variance represented; |z| ≥ 3 in 565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.6 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.2 | +4.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.9 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.0 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -11.9 | -7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.8 | -7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -10.6 | -7.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.0 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | LEO1 component of Paf1/RNA polymerase II complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:51,938,025-51,971,778 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Paf1/RNA polymerase II complex |
| Reactome | 20 pathways, smallest: Dengue virus activates/modulates innate and adaptive immune responses; Formation of the beta-catenin:TCF transactivating complex; E3 ubiquitin ligases ubiquitinate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVC0](https://www.uniprot.org/uniprotkb/Q8WVC0) (RNA polymerase-associated protein LEO1):

> Component of the PAF1 complex (PAF1C) which has multiple functions during transcription by RNA polymerase II and is implicated in regulation of development and maintenance of embryonic stem cell pluripotency. PAF1C associates with RNA polymerase II through interaction with POLR2A CTD non-phosphorylated and 'Ser-2'- and 'Ser-5'-phosphorylated forms and is involved in transcriptional elongation, acting both independently and synergistically with TCEA1 and in cooperation with the DSIF complex and …

**Summary**, from NCBI Gene [123169](https://www.ncbi.nlm.nih.gov/gene/123169):

> LEO1, parafibromin (CDC73; MIM 607393), CTR9 (MIM 609366), and PAF1 (MIM 610506) form the PAF protein complex that associates with the RNA polymerase II subunit POLR2A (MIM 180660) and with a histone methyltransferase complex (Rozenblatt-Rosen et al., 2005 [PubMed 15632063]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30401) · Entrez [123169](https://www.ncbi.nlm.nih.gov/gene/123169) · UniProt [Q8WVC0](https://www.uniprot.org/uniprotkb/Q8WVC0) · Ensembl [ENSG00000166477](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166477)

## Data

Gene col 9316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9316); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9316]; `tensor/DDL_lfc|DDL_z.npy` [9316]; `embed/gene_vectors.npy` [9316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9316 or target_col == 9316). Every well: [[LEO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LEO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
