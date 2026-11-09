---
symbol: "IFIT5"
type: "gene"
col: 7657
ensembl_id: "ENSG00000152778"
name: "interferon induced protein with tetratricopeptide repeats 5"
location: "10q23.31"
module: 32
arm: "+"
pooled_cpm: 17.35
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 32
n_dd_up_clean: 24
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 71
direction_downstream: 33
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFIT5

*interferon induced protein with tetratricopeptide repeats 5* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 3.73× (z +13.9, q 3e-41, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.256× (z -14.4, q 5e-44, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTX3L]] (+0.92, fdr 7e-06), [[PARP14]] (+0.90, fdr 7e-06), [[TRIM21]] (+0.90, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 71 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 33 go from it, the strongest it → [[IRF9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 1 with an alert ⚠; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **3.73×** | +13.9 | 3e-41 | 44/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.56×** | +9.9 | 8e-21 | 37/45 (CFPAC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.10×** | +7.6 | 7e-12 | 32/46 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.04×** | +7.5 | 7e-12 | 33/46 (A-172, HS-578T, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.81×** | +6.3 | 4e-08 | 34/47 (CFPAC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.60×** | +4.8 | 1e-04 | 23/45 (RKO, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.0 | 0.006 | 21/44 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.007 | 15/47 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.007 | 22/45 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.43×** | +3.8 | 0.009 | 13/48 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.009 | 16/45 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.42×** | +3.7 | 0.009 | 16/47 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.010 | 22/46 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.011 | 15/47 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.019 | 14/47 (CFPAC-1, HT-29, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7657.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.256×** | -14.4 | 5e-44 | 41/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.271×** | -13.8 | 1e-40 | 38/47 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.279×** | -13.5 | 4e-39 | 44/47 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.429×** | -12.6 | 3e-34 | 34/47 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.402×** | -9.6 | 8e-20 | 35/44 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.527×** | -9.6 | 1e-19 | 33/48 (COLO 205, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.456×** | -8.3 | 9e-15 | 28/45 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.478×** | -7.8 | 5e-13 | 34/46 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.483×** | -7.7 | 1e-12 | 34/45 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.497×** | -7.4 | 1e-11 | 36/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.498×** | -7.3 | 1e-11 | 27/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.517×** | -6.9 | 2e-10 | 31/48 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.523×** | -6.8 | 4e-10 | 31/45 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.643×** | -6.6 | 2e-09 | 29/47 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.545×** | -6.4 | 6e-09 | 31/47 (BT-474, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.600×** | -5.4 | 2e-06 | 27/45 (CHP-212, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 23.1 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0280× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.113× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 30.2 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0842× (z -16.7) |
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 10 (2 ⚠) | — | [[Tofacitinib (drug)]] 0.5 µM 0.0767× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 36.6 | 2 | 7 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 5.47× (z +10.7) | [[Tofacitinib (drug)]] 5 µM 0.243× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 29.9 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0672× (z -15.7) |
| [[A-172 (line)]] | wt | 40.4 | 3 | 4 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.48× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.0813× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 33.5 | 2 | 4 | [[Harringtonine (drug)]] 0.5 µM 5.15× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.0812× (z -17.1) |
| [[A549 (line)]] | wt | 25.2 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.131× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0561× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.193× (z -11.5) |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0583× (z -12.8) |
| [[COLO 205 (line)]] | alt | 42.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0898× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 33.6 | 0 | 5 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.223× (z -12.2) |
| [[RKO (line)]] | wt | 25.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0494× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -9.8) |
| [[HS-578T (line)]] | alt | 13.0 | 2 | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.99× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.104× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.129× (z -9.2) |
| [[C32 (line)]] | wt | 10.3 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 12.2× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0924× (z -12.7) |
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.131× (z -11.4) |
| [[A498 (line)]] | wt | 15.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -9.0) |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0750× (z -9.2) |
| [[Hs 766T (line)]] | wt | 25.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -10.1) |
| [[KATO III (line)]] | alt | 19.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.296× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 10.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.239× (z -9.2) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 32.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0735× (z -12.8) |
| [[A-427 (line)]] | wt | 5.04 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0994× (z -9.3) |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0605× (z -12.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 10.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0443× (z -10.6) |
| [[LS 180 (line)]] | wt | 8.36 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 5.47 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0868× (z -10.0) |
| [[PANC-1 (line)]] | alt | 10.1 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 6.96× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.288× (z -8.5) |
| [[SW 900 (line)]] | alt | 5.31 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0431× (z -9.5) |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTX3L]] | +0.92 | +0.88 / +0.93 | both halves | 7e-06 | **novel candidate** |
| [[PARP14]] | +0.90 | +0.86 / +0.90 | both halves | 7e-06 | STRING 469 |
| [[TRIM21]] | +0.90 | +0.83 / +0.91 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 499 |
| [[HERC6]] | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | STRING 734 |
| [[IFIT3]] | +0.88 | +0.86 / +0.88 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 857; ⚠ same locus (37.1 kb, same strand: neighbours can correlate without regulation) |
| [[IFIT1]] | +0.87 | +0.84 / +0.90 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 846; ⚠ same locus (8.1 kb, same strand: neighbours can correlate without regulation) |
| [[PARP9]] | +0.87 | +0.80 / +0.91 | both halves | 7e-06 | STRING 653 |
| [[NMI]] | +0.87 | +0.81 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[DDX60L]] | +0.87 | +0.82 / +0.87 | both halves | 7e-06 | STRING 600 |
| [[MX1]] | +0.87 | +0.83 / +0.90 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 883 |
| [[OAS2]] | +0.87 | +0.81 / +0.90 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 816 |
| [[XAF1]] | +0.86 | +0.77 / +0.90 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 683 |
| [[SAMD9]] | +0.86 | +0.82 / +0.89 | both halves | 7e-06 | STRING 665 |
| [[SAMD9L]] | +0.86 | +0.79 / +0.90 | both halves | 7e-06 | STRING 687 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 40, C 31. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises IFIT5's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without OAS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS1]] | B | OAS1 activity raises IFIT5's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without OAS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity raises IFIT5's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.21× lower at baseline in the lines without IFI6 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises IFIT5's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.82× lower at baseline in the lines without TRIM22 | 0.005 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[OAS2]] | B | OAS2 activity strengthens IFIT5's drug response | lines that do not express OAS2 (14) vs lines expressing it (34) | the lines without OAS2 respond 0.46× as strongly (z diff +1.98); strongest at Panobinostat 5 µM: 0.51x vs 0.21x (z diff +4.0) | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[FBXO39]] | B | FBXO39 activity raises IFIT5's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.87× lower at baseline in the lines without FBXO39 | 0.007 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[OAS3]] | B | OAS3 activity raises IFIT5's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.65× lower at baseline in the lines without OAS3 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[SAMD9L]] | B | SAMD9L activity raises IFIT5's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.69× lower at baseline in the lines without SAMD9L | 0.014 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[MX1]] | B | MX1 activity raises IFIT5's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without MX1 | 0.015 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFI6]] | B | IFI6 activity strengthens IFIT5's drug response | lines that do not express IFI6 (13) vs lines expressing it (35) | the lines without IFI6 respond 0.43× as strongly (z diff +2.15); strongest at Panobinostat 5 µM: 0.51x vs 0.22x (z diff +4.0) | 0.016 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[GBP4]] | B | GBP4 activity raises IFIT5's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without GBP4 | 0.021 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[CMPK2]] | B | CMPK2 activity raises IFIT5's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without CMPK2 | 0.023 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 0, C 33. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF9]] | C | IFIT5's natural level strengthens IRF9's drug response | IFIT5's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.78, reverse +0.75; direction not clear | 3e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | IFIT5's natural level strengthens ADAR's drug response | IFIT5's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.81; direction not clear | 5e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFI35]] | C | IFIT5's natural level strengthens IFI35's drug response | IFIT5's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.80, reverse +0.76; direction not clear | 9e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | IFIT5's natural level strengthens PARP12's drug response | IFIT5's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.77; direction not clear | 1e-03 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRANK1]] | C | IFIT5's natural level strengthens TRANK1's drug response | IFIT5's natural level across 41 lines (lineage-adjusted; a glimpse) | r +0.81, reverse +0.57; direction not clear | 0.001 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | IFIT5's natural level strengthens PARP10's drug response | IFIT5's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.72; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | IFIT5's natural level strengthens TRIM25's drug response | IFIT5's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.68; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | IFIT5's natural level strengthens HELZ2's drug response | IFIT5's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.77; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | IFIT5's natural level strengthens USP18's drug response | IFIT5's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.77; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | IFIT5's natural level strengthens PML's drug response | IFIT5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.73; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | IFIT5's natural level strengthens IFIT1's drug response | IFIT5's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.58; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | IFIT5's natural level strengthens TDRD7's drug response | IFIT5's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.64; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.890). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.1, 54.1); signed map (63.4, 32.3). **Vector** length 145, 47.2% of its response variance represented; |z| ≥ 3 in 1,450 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.73 to 56); *interferon gamma response* (hallmark, mean cos +0.75 to 60); *interferon* (control, mean cos +0.80 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +14.5 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.0 | +9.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.4 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.6 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.4 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +1.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.6 | -12.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.3 | -9.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.9 | -8.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.8 | -6.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.3 | -7.3 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced protein with tetratricopeptide repeats 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:89,414,568-89,421,605 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RI58 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Reactome | 5 pathways, smallest: IFIT antiviral response; Interferon alpha/beta signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13325](https://www.uniprot.org/uniprotkb/Q13325) (Interferon-induced protein with tetratricopeptide repeats 5):

> Interferon-induced RNA-binding protein involved in the human innate immune response. Has a broad and adaptable RNA structure recognition important for RNA recognition specificity in antiviral defense. Binds precursor and processed tRNAs as well as poly-U-tailed tRNA fragments. Specifically binds single-stranded RNA bearing a 5'-triphosphate group (PPP-RNA), thereby acting as a sensor of viral single-stranded RNAs. Single-stranded PPP-RNAs, which lack 2'-O-methylation of the 5' cap and bear a …

**Summary**, from NCBI Gene [24138](https://www.ncbi.nlm.nih.gov/gene/24138):

> Enables RNA binding activity and double-stranded DNA binding activity. Involved in defense response to virus; negative regulation of viral genome replication; and positive regulation of canonical NF-kappaB signal transduction. Located in several cellular components, including IkappaB kinase complex; actin cytoskeleton; and ruffle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13328) · Entrez [24138](https://www.ncbi.nlm.nih.gov/gene/24138) · UniProt [Q13325](https://www.uniprot.org/uniprotkb/Q13325) · Ensembl [ENSG00000152778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152778)

## Data

Gene col 7657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7657); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7657]; `tensor/DDL_lfc|DDL_z.npy` [7657]; `embed/gene_vectors.npy` [7657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7657 or target_col == 7657). Every well: [[IFIT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFIT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
