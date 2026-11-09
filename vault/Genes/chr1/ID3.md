---
symbol: "ID3"
type: "gene"
col: 3895
ensembl_id: "ENSG00000117318"
name: "inhibitor of DNA binding 3"
location: "1p36.12"
module: 11
arm: "+"
pooled_cpm: 25.29
n_lines_expressing: 40
n_dd_up: 3
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ID3

*inhibitor of DNA binding 3* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.27× (z +4.8, q 0.001, up in 24 of 38 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 6.51×, SNU-1 7.43×; ⚠ cell-cycle shift, explains ~47% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (SNU-1 12.6×; ⚠ cell-cycle shift, explains ~25% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A498 7.01×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.416× (z -7.5, q 4e-11, down in 29 of 37 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ID4]] (+0.62, fdr 1e-05), [[SAMD11]] (+0.58, fdr 1e-05), [[C2orf74-DT]] (+0.58, fdr 2e-05); moves opposite to [[SMG1P6]] (-0.59, fdr 3e-05), [[PLEKHH1]] (-0.53, fdr 3e-05), [[SPTLC1]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MSX2]] → it (grade B ⚠); 4 go from it, the strongest it → [[THOC5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3895.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 6.51×, SNU-1 7.43×; ⚠ cell-cycle shift, explains ~47% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (SNU-1 12.6×; ⚠ cell-cycle shift, explains ~25% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A498 7.01×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.27×** | +4.8 | 0.001 | 24/38 (NCI-H2030, SNU-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **2.16×** | +4.5 | 0.002 | 25/37 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.80×** | +3.5 | 0.073 | 20/38 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.46× | +3.2 | 0.18 | 17/38 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.64× | +3.0 | 0.23 | 15/37 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3895.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.416×** | -7.5 | 4e-11 | 29/37 (AN3 CA, C-33 A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.551×** | -3.4 | 0.089 | 18/38 (SHP-77, NCI-H1792, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.559×** | -3.4 | 0.089 | 21/37 (hTERT-HPNE, SHP-77, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.350×** | -3.3 | 0.089 | 18/34 (A-427, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.580×** | -3.3 | 0.089 | 21/37 (H4, LS 180, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.356×** | -3.3 | 0.089 | 22/38 (SNU-423, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.585×** | -3.2 | 0.089 | 20/37 (SHP-77, MIA PaCa-2, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.588×** | -3.2 | 0.089 | 19/38 (H4, C-33 A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.588×** | -3.2 | 0.089 | 18/37 (HOP62, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 172 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0443× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -14.0) |
| [[A-172 (line)]] | wt | 63.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -8.5) |
| [[AN3 CA (line)]] | alt | 164 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0770× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -12.5) |
| [[SNU-1 (line)]] | wt | 106 | 2 (2 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 12.6× (z +12.2) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 87.9 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 6.51× (z +9.4) ⚠ cell-cycle shift, explains ~47% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 73.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0410× (z -14.7) |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0226× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0803× (z -12.3) |
| [[SHP-77 (line)]] | alt | 30.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0961× (z -13.3) |
| [[A498 (line)]] | wt | 23.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.01× (z +9.6) | — |
| [[H4 (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0274× (z -11.8) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HepG2_C3A (line)]] | wt | 23.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 39.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 49.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -10.1) |
| [[A-427 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ID4]] | +0.62 | +0.52 / +0.68 | both halves | 1e-05 | same gene group; pathway: NGF-stimulated transcription |
| [[SAMD11]] | +0.58 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[C2orf74-DT]] | +0.58 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[TMEM70]] | +0.55 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[PIGBOS1]] | +0.55 | +0.32 / +0.62 | both halves | 2e-04 |  |
| [[KAT6A]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ARMCX2]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ZSCAN18]] | +0.53 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[EID2]] | +0.53 | +0.39 / +0.66 | both halves | 6e-05 |  |
| [[ID2]] | +0.53 | +0.48 / +0.57 | both halves | 2e-05 | same gene group; pathway: HALLMARK_TGF_BETA_SIGNALING; STRING 545 |
| [[MED13L]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[MRPL57]] | +0.52 | +0.31 / +0.62 | both halves | 2e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P6]] | -0.59 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[PLEKHH1]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[SPTLC1]] | -0.52 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[CTTN]] | -0.51 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[BPNT2]] | -0.50 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[TMEM181]] | -0.50 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[THOC5]] | -0.50 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[TM9SF3]] | -0.49 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[PIGG]] | -0.48 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[SELENOF]] | -0.48 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[PDCD6P1]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[LY6G5B]] | -0.48 | -0.16 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[TPD52L2]] | -0.47 | -0.30 / -0.60 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX2]] | B | MSX2 activity lowers ID3's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 2.92× higher at baseline in the lines without MSX2 | 0.078 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[ID4]] | B | ID4 activity raises ID3's level | lines that do not express ID4 (25) vs lines expressing it (25) | 3.15× lower at baseline in the lines without ID4 | 0.087 | ⚠ within organs, on part of the lines; also absent: CCDC144NL-AS1, ENSG00000264660, ENSG00000289911 |
| [[SAMD11]] | C | SAMD11 activity raises ID3's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 5.62× lower at baseline in the lines without SAMD11 | 0.027 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THOC5]] | B | ID3 activity raises THOC5's level | lines that do not express ID3 (10) vs lines expressing it (40) | 1.33× lower at baseline in the lines without ID3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SAMD11, TTC28, ITPR1 |
| [[EPC1]] | B | ID3 activity raises EPC1's level | lines that do not express ID3 (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without ID3 | 0.073 | ⚠ within organs, on part of the lines; also absent: SAMD11, TTC28, ITPR1 |
| [[MXRA7]] | B | ID3 activity raises MXRA7's level | lines that do not express ID3 (10) vs lines expressing it (40) | 2.91× lower at baseline in the lines without ID3 | 0.093 | ⚠ within organs, on part of the lines; also absent: SAMD11, TTC28, ITPR1 |
| [[ADNP2]] | B | ID3 activity raises ADNP2's level | lines that do not express ID3 (10) vs lines expressing it (40) | 1.19× lower at baseline in the lines without ID3 | 0.0995 | ⚠ within organs, on part of the lines; also absent: SAMD11, TTC28, ITPR1 |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.0, 40.3); signed map (6.6, -12.6). **Vector** length 95.7, 27.6% of its response variance represented; |z| ≥ 3 in 732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.9 | +4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +4.5 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.3 | +2.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | -0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -1.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of DNA binding 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:23,557,926-23,559,501 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HEIR-1, bHLHb25 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; Inhibitor of DNA binding family |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 5 pathways, smallest: NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation); Signaling by NTRK1 (TRKA) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02535](https://www.uniprot.org/uniprotkb/Q02535) (DNA-binding protein inhibitor ID-3):

> Transcriptional regulator (lacking a basic DNA binding domain) which negatively regulates the basic helix-loop-helix (bHLH) transcription factors by forming heterodimers and inhibiting their DNA binding and transcriptional activity. Implicated in regulating a variety of cellular processes, including cellular growth, senescence, differentiation, apoptosis, angiogenesis, and neoplastic transformation. Involved in myogenesis by inhibiting skeletal muscle and cardiac myocyte differentiation and …

**Summary**, from NCBI Gene [3399](https://www.ncbi.nlm.nih.gov/gene/3399):

> The protein encoded by this gene is a helix-loop-helix (HLH) protein that can form heterodimers with other HLH proteins. However, the encoded protein lacks a basic DNA-binding domain and therefore inhibits the DNA binding of any HLH protein with which it interacts. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:5362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5362) · Entrez [3399](https://www.ncbi.nlm.nih.gov/gene/3399) · UniProt [Q02535](https://www.uniprot.org/uniprotkb/Q02535) · Ensembl [ENSG00000117318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117318)

## Data

Gene col 3895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3895); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3895]; `tensor/DDL_lfc|DDL_z.npy` [3895]; `embed/gene_vectors.npy` [3895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3895 or target_col == 3895). Every well: [[ID3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ID3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
