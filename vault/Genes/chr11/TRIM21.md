---
symbol: "TRIM21"
type: "gene"
col: 5274
ensembl_id: "ENSG00000132109"
name: "tripartite motif containing 21"
location: "11p15.4"
module: 32
arm: "+"
pooled_cpm: 10.65
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 29
n_dd_up_clean: 16
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 29
direction_downstream: 13
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TRIM21

*tripartite motif containing 21* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.70× (z +11.6, q 3e-28, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.296× (z -14.1, q 1e-42, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT5]] (+0.90, fdr 7e-06), [[DTX3L]] (+0.88, fdr 7e-06), [[DDX60L]] (+0.87, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[PLSCR1]] → it (grade B ⚠); 13 go from it, the strongest it → [[IFIT5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5274.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.70×** | +11.6 | 3e-28 | 38/45 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +7.3 | 7e-11 | 27/42 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +7.0 | 6e-10 | 25/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.1 | 2e-07 | 22/47 (hTERT-HPNE, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +5.5 | 5e-06 | 24/46 (NCI-H2347, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 6e-05 | 16/44 (CFPAC-1, LoVo, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +4.5 | 6e-04 | 20/46 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.007 | 13/44 (AsPC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.40×** | +3.7 | 0.014 | 12/46 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.021 | 10/46 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.021 | 9/47 (A-172, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.4 | 0.031 | 15/42 (A-172, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.044 | 14/45 (LoVo, J82, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.048 | 14/42 (SNU-423, AsPC-1, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +3.2 | 0.048 | 7/40 (HS-578T, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.048 | 10/47 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5274.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.296×** | -14.1 | 1e-42 | 43/47 (A549, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.340×** | -12.5 | 1e-33 | 41/46 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.356×** | -12.0 | 5e-31 | 38/46 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.465×** | -8.5 | 2e-15 | 27/37 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.504×** | -8.0 | 2e-13 | 29/42 (SNU-423, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.618×** | -7.9 | 2e-13 | 28/47 (AsPC-1, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.517×** | -7.7 | 1e-12 | 24/33 (LoVo, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.519×** | -7.0 | 1e-10 | 21/25 (A549, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.654×** | -7.0 | 2e-10 | 29/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.564×** | -6.7 | 2e-09 | 28/46 (SNU-423, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.590×** | -6.1 | 4e-08 | 25/47 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -6.0 | 9e-08 | 22/46 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.610×** | -5.7 | 4e-07 | 23/43 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.637×** | -5.2 | 7e-06 | 22/44 (MIA PaCa-2, LoVo, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.634×** | -5.0 | 2e-05 | 23/44 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.740×** | -5.0 | 2e-05 | 22/47 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.653×** | -5.0 | 2e-05 | 22/46 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.461×** | -4.7 | 8e-05 | 18/45 (A-172, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 21.4 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0883× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.121× (z -12.1) |
| [[LoVo (line)]] | wt | 12.1 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0419× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.166× (z -10.5) |
| [[SNU-423 (line)]] | alt | 25.3 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -11.6) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.161× (z -10.8) |
| [[A-172 (line)]] | wt | 21.6 | 1 | 3 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.45× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.222× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.129× (z -10.7) |
| [[PANC-1 (line)]] | alt | 14.2 | 2 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 8.20× (z +16.0) | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -10.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.177× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 11.6 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 7.63× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -9.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0872× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.145× (z -8.5) |
| [[BT-474 (line)]] | alt | 7.60 | 0 | 2 | — | [[Neratinib (drug)]] 0.05 µM 0.0968× (z -8.8) |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0811× (z -11.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 9.17 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0568× (z -10.0) |
| [[H4 (line)]] | wt | 12.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0400× (z -11.8) |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.0514× (z -10.4) |
| [[HS-578T (line)]] | alt | 8.32 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 8.58 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.148× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 4.99 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.102× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 6.09 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -10.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 5.97 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT5]] | +0.90 | +0.83 / +0.91 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 499 |
| [[DTX3L]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[DDX60L]] | +0.87 | +0.83 / +0.86 | both halves | 7e-06 | STRING 437 |
| [[IFIT3]] | +0.86 | +0.79 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 595 |
| [[PARP14]] | +0.86 | +0.81 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SAMD9L]] | +0.85 | +0.78 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 511 |
| [[SAMD9]] | +0.85 | +0.80 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 531 |
| [[HERC6]] | +0.84 | +0.77 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 503 |
| [[PARP9]] | +0.84 | +0.77 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 609 |
| [[DDX60]] | +0.84 | +0.79 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 482 |
| [[IFIH1]] | +0.83 | +0.80 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 812 |
| [[NMI]] | +0.83 | +0.74 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 719 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 19, C 10. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR1]] | B | PLSCR1 activity raises TRIM21's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 1.91× lower at baseline in the lines without PLSCR1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity raises TRIM21's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without BATF2 | 0.011 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises TRIM21's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without OAS2 | 0.021 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[SAMD9]] | B | SAMD9 activity raises TRIM21's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.63× lower at baseline in the lines without SAMD9 | 0.027 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[RSAD2]] | B | RSAD2 activity raises TRIM21's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without RSAD2 | 0.028 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[IFI6]] | B | IFI6 activity raises TRIM21's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without IFI6 | 0.029 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[SP110]] | B | SP110 activity raises TRIM21's level | lines that do not express SP110 (5) vs lines expressing it (45) | 2.05× lower at baseline in the lines without SP110 | 0.038 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[DDX60]] | B | DDX60 activity raises TRIM21's level | lines that do not express DDX60 (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without DDX60 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, RNASEL, SAMD9; maybe low, not absent |
| [[OAS3]] | B | OAS3 activity raises TRIM21's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without OAS3 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[DDX60L]] | B | DDX60L activity raises TRIM21's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 1.69× lower at baseline in the lines without DDX60L | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises TRIM21's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.40× lower at baseline in the lines without MX1 | 0.050 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[PARP9]] | B | PARP9 activity raises TRIM21's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without PARP9 | 0.050 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT5]] | C | TRIM21's natural level strengthens IFIT5's drug response | TRIM21's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.71; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | TRIM21's natural level strengthens TDRD7's drug response | TRIM21's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.57; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ZC3HAV1]] | C | TRIM21's natural level strengthens ZC3HAV1's drug response | TRIM21's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.29; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NMI]] | C | TRIM21's natural level strengthens NMI's drug response | TRIM21's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.60; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFI35]] | C | TRIM21's natural level strengthens IFI35's drug response | TRIM21's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.64; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRANK1]] | C | TRIM21's natural level strengthens TRANK1's drug response | TRIM21's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.43; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[APOL2]] | C | TRIM21's natural level strengthens APOL2's drug response | TRIM21's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.37; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PHF11]] | C | TRIM21's natural level strengthens PHF11's drug response | TRIM21's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.41; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ZNFX1]] | C | TRIM21's natural level strengthens ZNFX1's drug response | TRIM21's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.43; direction not clear | 0.069 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TAP1]] | C | TRIM21's natural level strengthens TAP1's drug response | TRIM21's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.61; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[HERC6]] | C | TRIM21's natural level strengthens HERC6's drug response | TRIM21's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.59; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | TRIM21's natural level strengthens PARP12's drug response | TRIM21's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.53; direction not clear | 0.092 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.866). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.6, 54.1); signed map (62.9, 32.3). **Vector** length 111, 28.2% of its response variance represented; |z| ≥ 3 in 1,235 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.77 to 23); *Interferon alpha/beta signaling* (reactome, mean cos +0.74 to 27); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.77 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.7 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.5 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.0 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.7 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.3 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +3.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.6 | -7.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.3 | -7.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.1 | -5.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.0 | -7.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.8 | -6.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.4 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:4,384,897-4,393,702 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRIM21/Ro52, RNF81, RO52; previously SSA1 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 14 pathways, smallest: Regulation of innate immune responses to cytosolic DNA; STING mediated induction of host immune responses; Cytosolic sensors of pathogen-associated DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P19474](https://www.uniprot.org/uniprotkb/P19474) (E3 ubiquitin-protein ligase TRIM21):

> E3 ubiquitin-protein ligase whose activity is dependent on E2 enzymes, UBE2D1, UBE2D2, UBE2E1 and UBE2E2. Forms a ubiquitin ligase complex in cooperation with the E2 UBE2D2 that is used not only for the ubiquitination of USP4 and IKBKB but also for its self-ubiquitination. Component of cullin-RING-based SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complexes such as SCF(SKP2)-like complexes. A TRIM21-containing SCF(SKP2)-like complex is shown to mediate ubiquitination of CDKN1B …

**Summary**, from NCBI Gene [6737](https://www.ncbi.nlm.nih.gov/gene/6737):

> This gene encodes a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The encoded protein is part of the RoSSA ribonucleoprotein, which includes a single polypeptide and one of four small RNA molecules. The RoSSA particle localizes to both the cytoplasm and the nucleus. RoSSA interacts with autoantigens in patients with Sjogren syndrome and systemic lupus erythematosus. …

**Accessions** — [HGNC:11312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11312) · Entrez [6737](https://www.ncbi.nlm.nih.gov/gene/6737) · UniProt [P19474](https://www.uniprot.org/uniprotkb/P19474) · Ensembl [ENSG00000132109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132109)

## Data

Gene col 5274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5274); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5274]; `tensor/DDL_lfc|DDL_z.npy` [5274]; `embed/gene_vectors.npy` [5274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5274 or target_col == 5274). Every well: [[TRIM21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
