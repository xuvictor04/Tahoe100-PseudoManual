---
symbol: "FAM86DP"
type: "gene"
col: 14386
ensembl_id: "ENSG00000244026"
name: "family with sequence similarity 86 member D, pseudogene"
location: "3p12.3"
module: 18
arm: "+"
pooled_cpm: 3.51
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# FAM86DP

*family with sequence similarity 86 member D, pseudogene* — 3p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.65× (z +5.4, q 5e-05, up in 5 of 18 measured lines) ⚠ toxic. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.51× (z +4.5, q 0.001, up in 9 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.779× (z -3.9, q 0.035, down in 16 of 35 measured lines) ⚠ cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[Binimetinib (drug)]] 0.5 µM: 0.738× (z -3.8, q 0.035, down in 7 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SK-MEL-2 0.195×, HEC-1-A 0.329×, SW480 0.294×, NCI-H460 0.285×; ⚠ cell-cycle shift, explains ~67% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.202×, SW480 0.163×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0742×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0665×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM86DP-1]] (+0.70, fdr 7e-06, ⚠ same locus), [[RABEPK]] (+0.65, fdr 7e-06), [[NT5M]] (+0.64, fdr 7e-06), [[ARMC10]] (+0.59, fdr 1e-05); moves opposite to [[SMARCA5]] (-0.55, fdr 3e-05), [[SPDYA]] (-0.55, fdr 2e-05), [[BDH2]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.4 | 5e-05 | 5/18 (NCI-H1573, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.6 | 0.001 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +4.5 | 0.001 | 9/43 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +4.1 | 0.006 | 12/36 (AsPC-1, Panc 03.27, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.013 | 8/41 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +3.8 | 0.014 | 4/44 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Pentagastrin (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.027 | 3/39 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.4 | 0.042 | 0/11 | rises with dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14386.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (SK-MEL-2 0.195×, HEC-1-A 0.329×, SW480 0.294×, NCI-H460 0.285×; ⚠ cell-cycle shift, explains ~67% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.202×, SW480 0.163×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0742×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0665×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.779×** | -3.9 | 0.035 | 16/35 (SK-MEL-2, HEC-1-A, …) | top dose only | composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.738×** | -3.8 | 0.035 | 7/42 (HEC-1-A, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.552× | -3.4 | 0.11 | 5/23 (SW480, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.729× | -3.4 | 0.11 | 15/42 (A-172, HEC-1-A, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.730× | -3.3 | 0.11 | 7/41 (COLO 205, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.752× | -3.2 | 0.14 | 9/42 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Binimetinib (drug)]] 5 µM |  | 0.798× | -3.1 | 0.14 | 8/46 (C32, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 9.90 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[SW480 (line)]] | alt | 4.15 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 4.02 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0742× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 3.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -8.6) ⚠ cell-cycle shift, explains ~67% of this change |
| [[RPMI-7951 (line)]] | alt | 5.21 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0665× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.8) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM86DP-1]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RABEPK]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[NT5M]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ARMC10]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NSUN5P1]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[DPY19L3]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PGS1]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[FAM89A]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SLC15A4]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[FAM24B]] | +0.56 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[FAHD2A]] | +0.56 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[NBPF15]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[KDM4A-AS1]] | +0.55 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCA5]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[SPDYA]] | -0.55 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[BDH2]] | -0.52 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[ABCA10]] | -0.50 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[ELF1]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SYNE2]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[MAT2B]] | -0.49 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[PBX2]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TMEM107]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[DSP]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[IQCN]] | -0.47 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[FAM171B]] | -0.47 | -0.50 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.4, -18.2); signed map (-40.8, -21.0). **Vector** length 51.4, 6.46% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +1.8 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +1.5 | +3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.4 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.4 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.0 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -2.7 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 86 member D, pseudogene |
| Locus type | pseudogene |
| Location | 3p12.3 — chr3:75,422,961-75,435,110 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously FAM86D |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32659) · Entrez [692099](https://www.ncbi.nlm.nih.gov/gene/692099) · Ensembl [ENSG00000244026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244026)

## Data

Gene col 14386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14386); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14386]; `tensor/DDL_lfc|DDL_z.npy` [14386]; `embed/gene_vectors.npy` [14386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14386 or target_col == 14386). Every well: [[FAM86DP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM86DP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
