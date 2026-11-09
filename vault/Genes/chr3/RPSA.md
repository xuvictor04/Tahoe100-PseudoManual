---
symbol: "RPSA"
type: "gene"
col: 9584
ensembl_id: "ENSG00000168028"
name: "ribosomal protein SA"
location: "3p22.1"
module: 20
arm: "+"
pooled_cpm: 33.68
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RPSA

*ribosomal protein SA* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.17× (z +15.0, q 0e+00, up in 43 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.92× (z +7.3, q 4e-11, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Baicalin (drug)]] 0.5 µM: 0.705× (z -4.6, q 0.002, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNPS1]] (+0.79, fdr 7e-06), [[RPS3A]] (+0.76, fdr 7e-06), [[RPL6]] (+0.75, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.73, fdr 7e-06), [[NKAP]] (-0.73, fdr 7e-06), [[ZMYM5]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRTAP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.17×** | +15.0 | 0e+00 | 43/45 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +13.6 | 2e-39 | 35/39 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.81×** | +12.4 | 3e-33 | 44/45 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.92×** | +7.3 | 4e-11 | 42/48 (PANC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.87×** | +7.2 | 8e-11 | 36/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +6.3 | 3e-08 | 33/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.64×** | +6.2 | 5e-08 | 27/46 (SW480, HT-29, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +5.9 | 3e-07 | 26/34 (HEC-1-A, AsPC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +5.6 | 2e-06 | 34/47 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +5.5 | 3e-06 | 30/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.48×** | +5.1 | 2e-05 | 25/48 (NCI-H1792, HOP62, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.47×** | +5.0 | 2e-05 | 30/48 (NCI-H1792, PANC-1, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.7 | 1e-04 | 0/48 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 3e-04 | 22/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.41×** | +4.5 | 3e-04 | 20/48 (NCI-H1792, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.2 | 8e-04 | 22/48 (NCI-H460, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lopinavir (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.003 | 20/47 (CFPAC-1, HOP62, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.74×** | +3.7 | 0.005 | 14/47 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.007 | 18/48 (A498, SW480, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.016 | 18/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.020 | 17/48 (NCI-H460, HOP62, …) | inconsistent across doses | position effect removed |
| [[Uridine (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.062 | 13/48 (HOP62, NCI-H2347, …) | two highest doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.062 | 15/47 (SW48, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.062 | 14/48 (BT-474, A-172, …) | top dose only | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.062 | 12/47 (HOP62, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Lopinavir (drug)]] 0.5 µM |  | **1.25×** | +2.8 | 0.090 | 15/48 (A549, NCI-H1792, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Baicalin (drug)]] 0.5 µM |  | **0.705×** | -4.6 | 0.002 | 22/48 (LoVo, A498, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.702×** | -4.5 | 0.002 | 26/48 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.741×** | -3.9 | 0.012 | 17/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Baicalin (drug)]] 5 µM |  | **0.810×** | -3.9 | 0.012 | 23/48 (A-427, LoVo, …) | two highest doses | position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.843× | -3.2 | 0.15 | 14/48 (J82, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.794× | -3.0 | 0.19 | 7/48 (SK-MEL-2, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 27.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +11.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 24.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.45× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 65.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +13.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 38.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 31.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +10.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 23.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.0) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A549 (line)]] | wt | 37.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 39.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.53× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.36× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 46.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 15.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +9.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.7) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H1573 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0499× (z -9.3) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNPS1]] | +0.79 | +0.75 / +0.79 | both halves | 7e-06 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[RPS3A]] | +0.76 | +0.68 / +0.80 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL6]] | +0.75 | +0.68 / +0.82 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[DHFR]] | +0.75 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[EMC1]] | +0.75 | +0.66 / +0.75 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[RPL18A]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[PPT1]] | +0.73 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[RPL10]] | +0.73 | +0.70 / +0.71 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[IPO5]] | +0.73 | +0.63 / +0.76 | both halves | 7e-06 | pathway: Influenza Infection |
| [[TXNDC5]] | +0.73 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[PRPF8]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[AGO1]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.73 | -0.72 / -0.71 | both halves | 7e-06 |  |
| [[NKAP]] | -0.73 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.73 | -0.69 / -0.71 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.72 | -0.66 / -0.75 | both halves | 7e-06 |  |
| [[ING2]] | -0.71 | -0.61 / -0.74 | both halves | 7e-06 |  |
| [[EIF1B]] | -0.70 | -0.65 / -0.71 | both halves | 7e-06 | STRING 799 |
| [[PIGBOS1]] | -0.70 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[ERVK3-1]] | -0.69 | -0.52 / -0.74 | both halves | 1e-05 |  |
| [[GGNBP2]] | -0.69 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[MED19]] | -0.68 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[MRPS18C]] | -0.68 | -0.58 / -0.67 | both halves | 7e-06 | STRING 598 |
| [[KRTCAP2]] | -0.67 | -0.57 / -0.70 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRTAP]] | C | CRTAP activity raises RPSA's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without CRTAP | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.879). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.3, -25.3); signed map (-21.9, -35.9). **Vector** length 102, 24.6% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +15.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +7.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -5.9 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -2.9 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +0.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.3 | -1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | -1.0 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein SA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:39,406,716-39,426,255 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LRP, 37LRP, p40, SA, uS2; previously LAMR1 |
| Gene groups (HGNC) | S ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 53 pathways, smallest: SARS-CoV-1 modulates host translation machinery; Dengue Virus Attachment and Entry; SARS-CoV-2 modulates host translation machinery |
| Matched by | ensembl_id |

**Function**, from UniProt [P08865](https://www.uniprot.org/uniprotkb/P08865) (Small ribosomal subunit protein uS2):

> Required for the assembly and/or stability of the 40S ribosomal subunit. Required for the processing of the 20S rRNA-precursor to mature 18S rRNA in a late step of the maturation of 40S ribosomal subunits. Also functions as a cell surface receptor for laminin. Plays a role in cell adhesion to the basement membrane and in the consequent activation of signaling transduction pathways. May play a role in cell fate determination and tissue morphogenesis. Acts as a PPP1R16B-dependent substrate of …

**Summary**, from NCBI Gene [3921](https://www.ncbi.nlm.nih.gov/gene/3921):

> Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Many of the effects of laminin are mediated through interactions with cell surface receptors. These receptors include members of the integrin family, as well as non-integrin laminin-binding proteins. This gene …

**Accessions** — [HGNC:6502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6502) · Entrez [3921](https://www.ncbi.nlm.nih.gov/gene/3921) · UniProt [P08865](https://www.uniprot.org/uniprotkb/P08865) · Ensembl [ENSG00000168028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168028)

## Data

Gene col 9584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9584); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9584]; `tensor/DDL_lfc|DDL_z.npy` [9584]; `embed/gene_vectors.npy` [9584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9584 or target_col == 9584). Every well: [[RPSA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPSA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
