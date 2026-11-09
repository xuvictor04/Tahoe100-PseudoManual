---
symbol: "ENOPH1"
type: "gene"
col: 6973
ensembl_id: "ENSG00000145293"
name: "enolase-phosphatase 1"
location: "4q21.22"
module: 20
arm: "+"
pooled_cpm: 25.48
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ENOPH1

*enolase-phosphatase 1* — 4q21.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.39× (z +17.1, q 0e+00, up in 35 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.25× (z +12.2, q 6e-32, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.284×; ⚠ cell-cycle shift, explains ~0% of this change); [[Allantoin (drug)]] 0.05 µM in 1 line (SNU-1 0.221×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COLGALT1]] (+0.65, fdr 7e-06), [[GPD1L]] (+0.64, fdr 7e-06), [[RPSA]] (+0.64, fdr 7e-06); moves opposite to [[IER5]] (-0.68, fdr 7e-06), [[ZKSCAN1]] (-0.60, fdr 1e-05), [[JUND]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BMP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 19 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.39×** | +17.1 | 0e+00 | 35/43 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.61×** | +13.3 | 9e-38 | 40/48 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.93×** | +12.9 | 8e-36 | 45/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.96×** | +12.8 | 3e-35 | 31/38 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.25×** | +12.2 | 6e-32 | 42/48 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.81×** | +11.7 | 1e-29 | 43/48 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.80×** | +11.6 | 4e-29 | 37/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.68×** | +10.2 | 9e-23 | 38/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.29×** | +8.5 | 9e-16 | 30/47 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.56×** | +8.1 | 3e-14 | 26/40 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.53×** | +8.0 | 5e-14 | 31/46 (HepG2/C3A, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +7.8 | 4e-13 | 30/46 (LOX-IMVI, SW1417, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.49×** | +7.6 | 2e-12 | 29/46 (A-427, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.48×** | +7.4 | 8e-12 | 30/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.42×** | +6.8 | 3e-10 | 26/46 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +6.2 | 2e-08 | 28/48 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.2 | 2e-08 | 20/48 (NCI-H1792, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.47×** | +5.4 | 2e-06 | 16/48 (SW1417, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.69×** | +5.4 | 2e-06 | 25/47 (HT-29, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.68×** | +5.4 | 2e-06 | 22/46 (CFPAC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.31×** | +5.2 | 4e-06 | 23/48 (LS 180, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.5 | 1e-04 | 15/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.55×** | +4.5 | 1e-04 | 12/47 (NCI-H460, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +4.5 | 2e-04 | 15/48 (HT-29, C-33 A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +4.1 | 7e-04 | 8/48 (NCI-H460, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.002 | 16/48 (NCI-H1573, A498, …) | rises with dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.8 | 0.002 | 12/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6973.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.284×; ⚠ cell-cycle shift, explains ~0% of this change); [[Allantoin (drug)]] 0.05 µM in 1 line (SNU-1 0.221×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 5 µM |  | 0.838× | -3.5 | 0.11 | 12/48 (A-427, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.851× | -3.5 | 0.11 | 12/48 (HepG2/C3A, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.842× | -3.5 | 0.11 | 17/48 (AN3 CA, SHP-77, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.798× | -3.2 | 0.19 | 14/47 (Panc 03.27, Hs 766T, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.747× | -3.0 | 0.27 | 8/45 (H4, KATO III, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 28.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 30.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[H4 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[PANC-1 (line)]] | alt | 32.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.22× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-1 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.221× (z -8.7) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLGALT1]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[GPD1L]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[RPSA]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[UTP18]] | +0.63 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[MTRR]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[ERLIN1]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[TATDN2]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[FAR1]] | +0.63 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[RPE]] | +0.62 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[GCSH]] | +0.62 | +0.65 / +0.57 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[PAICS]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ABCB10]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER5]] | -0.68 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[ZKSCAN1]] | -0.60 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[JUND]] | -0.58 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | -0.57 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[DYNLL1]] | -0.57 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[RBBP6]] | -0.56 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[ERVK3-1]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[CDK3]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[EIF1B]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[BRD2]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[IL10RB]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PNRC1]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP2]] | B | BMP2 activity lowers ENOPH1's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.26× higher at baseline in the lines without BMP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-22.5, -26.2); signed map (-41.1, -15.4). **Vector** length 91.7, 21.0% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.5 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +4.2 | +12.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +4.0 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +8.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.9 | +5.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +0.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | enolase-phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.22 — chr4:82,430,590-82,461,177 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MASA, E1, mtnC |
| Gene groups (HGNC) | HAD Asp-based non-protein phosphatases |
| Reactome | 3 pathways, smallest: Methionine salvage pathway; Sulfur amino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHY7](https://www.uniprot.org/uniprotkb/Q9UHY7) (Enolase-phosphatase E1):

> Bifunctional enzyme that catalyzes the enolization of 2,3-diketo-5-methylthiopentyl-1-phosphate (DK-MTP-1-P) into the intermediate 2-hydroxy-3-keto-5-methylthiopentenyl-1-phosphate (HK-MTPenyl-1-P), which is then dephosphorylated to form the acireductone 1,2-dihydroxy-3-keto-5-methylthiopentene (DHK-MTPene).

**Summary**, from NCBI Gene [58478](https://www.ncbi.nlm.nih.gov/gene/58478):

> Enables acireductone synthase activity. Involved in obsolete L-methionine salvage from methylthioadenosine. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24599) · Entrez [58478](https://www.ncbi.nlm.nih.gov/gene/58478) · UniProt [Q9UHY7](https://www.uniprot.org/uniprotkb/Q9UHY7) · Ensembl [ENSG00000145293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145293)

## Data

Gene col 6973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6973); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6973]; `tensor/DDL_lfc|DDL_z.npy` [6973]; `embed/gene_vectors.npy` [6973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6973 or target_col == 6973). Every well: [[ENOPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENOPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
