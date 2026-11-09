---
symbol: "ACKR3"
type: "gene"
col: 6885
ensembl_id: "ENSG00000144476"
name: "atypical chemokine receptor 3"
location: "2q37.3"
module: 14
arm: "+"
pooled_cpm: 3.88
n_lines_expressing: 20
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ACKR3

*atypical chemokine receptor 3* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.47× (z +10.9, q 8e-25, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.84× (z +5.3, q 1e-05, up in 13 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 10 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.258×, NCI-H460 0.274×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.127×; ⚠ cell-cycle shift, explains ~34% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.167×; ⚠ cell-cycle shift, would explain all of this change); [[HI-TOPK-032 (drug)]] 5 µM in 1 line (NCI-H1792 0.0393×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEIS1]] (+0.60, fdr 2e-05), [[IL6]] (+0.57, fdr 5e-05), [[ADAM28]] (+0.57, fdr 1e-05); moves opposite to [[PDS5A]] (-0.48, fdr 1e-04), [[KPNB1]] (-0.44, fdr 2e-04), [[MFSD14CP-1]] (-0.44, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[IGFN1]] → it (grade C ⚠); 9 go from it, the strongest it → [[GPCPD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.47×** | +10.9 | 8e-25 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.14×** | +8.0 | 3e-13 | 2/7 (A498, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +7.0 | 4e-10 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.90×** | +5.7 | 1e-06 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.84×** | +5.3 | 1e-05 | 13/15 (NCI-H460, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.02×** | +5.3 | 1e-05 | 3/10 (A-172, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +5.2 | 2e-05 | 2/13 (NCI-H460, A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +4.5 | 5e-04 | 6/16 (SW1417, SNU-423, …) | rises with dose |  |
| [[Vortioxetine (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.3 | 1e-03 | 2/14 (SNU-423, BT-474) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +4.3 | 1e-03 | 3/16 (A498, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.49×** | +4.2 | 0.001 | 5/15 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.0 | 0.003 | 1/13 (RPMI-7951) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +4.0 | 0.003 | 9/15 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.06×** | +3.9 | 0.004 | 2/11 (SNU-423, AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +3.7 | 0.009 | 10/17 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +3.6 | 0.011 | 4/14 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.93×** | +3.5 | 0.013 | 1/15 (A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.027 | 1/14 (CFPAC-1) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.027 | 0/13 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +3.2 | 0.032 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.042 | 5/15 (NCI-H460, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.76×** | +3.0 | 0.056 | 1/13 (NCI-H460) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Everolimus (drug)]] 0.05 µM |  | **1.35×** | +3.0 | 0.065 | 0/16 | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.065 | 2/16 (A549, NCI-H1792) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6885.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 10 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.258×, NCI-H460 0.274×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.127×; ⚠ cell-cycle shift, explains ~34% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.167×; ⚠ cell-cycle shift, would explain all of this change); [[HI-TOPK-032 (drug)]] 5 µM in 1 line (NCI-H1792 0.0393×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.625× | -3.3 | 0.49 | 1/17 (H4) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 71.6 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -19.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 9.93 | 3 | 1 | [[Harringtonine (drug)]] 0.5 µM 8.48× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -9.4) |
| [[A-172 (line)]] | wt | 3.59 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +9.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +9.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[AsPC-1 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 0.189 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.516 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEIS1]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[IL6]] | +0.57 | +0.40 / +0.63 | both halves | 5e-05 | pathway: HALLMARK_HYPOXIA |
| [[ADAM28]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[MAF]] | +0.56 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[PTGES]] | +0.53 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[TCIM]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[PEX5L]] | +0.53 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[HMGN2P46]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[IL1A]] | +0.52 | +0.44 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 439 |
| [[NINJ1]] | +0.52 | +0.43 / +0.57 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[C1QTNF1]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[SERPINB7]] | +0.52 | +0.34 / +0.66 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDS5A]] | -0.48 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[KPNB1]] | -0.44 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[MFSD14CP-1]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[GPR135]] | -0.43 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[IVD]] | -0.42 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[POLR3E]] | -0.42 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGFN1]] | C | IGFN1 activity raises ACKR3's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 3.56× lower at baseline in the lines without IGFN1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |
| [[BDKRB2]] | C | BDKRB2 activity raises ACKR3's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without BDKRB2 | 0.040 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003; co-absent with the target |
| [[SLC6A7]] | C | SLC6A7 activity raises ACKR3's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without SLC6A7 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9; co-absent with the target |
| [[CD38]] | C | CD38 activity raises ACKR3's level | lines that do not express CD38 (35) vs lines expressing it (15) | 2.57× lower at baseline in the lines without CD38 | 0.057 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent; co-absent with the target |
| [[CRTAC1]] | C | CRTAC1 activity raises ACKR3's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 2.34× lower at baseline in the lines without CRTAC1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; co-absent with the target |
| [[RHCG]] | C | RHCG activity raises ACKR3's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.57× lower at baseline in the lines without RHCG | 0.067 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPCPD1]] | B | ACKR3 activity raises GPCPD1's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without ACKR3 | 0.018 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1 |
| [[GPCPD1]] | B | ACKR3 activity weakens GPCPD1's drug response | lines that do not express ACKR3 (30) vs lines expressing it (19) | the lines without ACKR3 respond 1.21× as strongly (z diff -0.47); strongest at Homoharringtonine 5 µM: 2.60x vs 1.48x (z diff -3.7) | 0.060 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; target measured in part of the lines; both ways; artifact flags |
| [[PPP1R3B]] | B | ACKR3 activity raises PPP1R3B's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 1.54× lower at baseline in the lines without ACKR3 | 0.070 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1 |
| [[SLC16A6]] | C | ACKR3 activity raises SLC16A6's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 2.67× lower at baseline in the lines without ACKR3 | 0.031 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; co-absent with the target |
| [[ADAM28]] | C | ACKR3 activity raises ADAM28's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 2.69× lower at baseline in the lines without ACKR3 | 0.051 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; co-absent with the target |
| [[BDKRB2]] | C | ACKR3 activity raises BDKRB2's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 2.87× lower at baseline in the lines without ACKR3 | 0.054 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; co-absent with the target |
| [[CRTAC1]] | C | ACKR3 activity raises CRTAC1's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 2.96× lower at baseline in the lines without ACKR3 | 0.070 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; co-absent with the target |
| [[MAF]] | C | ACKR3 activity raises MAF's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 4.03× lower at baseline in the lines without ACKR3 | 0.075 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; co-absent with the target |
| [[XKR7]] | C | ACKR3 activity raises XKR7's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 1.41× lower at baseline in the lines without ACKR3 | 0.091 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.6, 19.6); signed map (49.8, 22.6). **Vector** length 45.5, 12.4% of its response variance represented; |z| ≥ 3 in 403 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.1 | -2.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | atypical chemokine receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:236,567,787-236,582,354 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RDC1, GPR159; previously CMKOR1, CXCR7 |
| Gene groups (HGNC) | Atypical chemokine receptors |
| Hallmark sets | HYPOXIA, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 7 pathways, smallest: Chemokine receptors bind chemokines; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P25106](https://www.uniprot.org/uniprotkb/P25106) (Atypical chemokine receptor 3):

> Atypical chemokine receptor that controls chemokine levels and localization via high-affinity chemokine binding that is uncoupled from classic ligand-driven signal transduction cascades, resulting instead in chemokine sequestration, degradation, or transcytosis. Also known as interceptor (internalizing receptor) or chemokine-scavenging receptor or chemokine decoy receptor. Acts as a receptor for chemokines CXCL11 and CXCL12/SDF1. Chemokine binding does not activate G protein-mediated signal …

**Summary**, from NCBI Gene [57007](https://www.ncbi.nlm.nih.gov/gene/57007):

> This gene encodes a member of the G-protein coupled receptor family. Although this protein was earlier thought to be a receptor for vasoactive intestinal peptide (VIP), it is now considered to be an orphan receptor, in that its endogenous ligand has not been identified. The protein is also a coreceptor for human immunodeficiency viruses (HIV). Translocations involving this gene and HMGA2 on chromosome 12 have been observed in lipomas. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23692](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23692) · Entrez [57007](https://www.ncbi.nlm.nih.gov/gene/57007) · UniProt [P25106](https://www.uniprot.org/uniprotkb/P25106) · Ensembl [ENSG00000144476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144476)

## Data

Gene col 6885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6885); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6885]; `tensor/DDL_lfc|DDL_z.npy` [6885]; `embed/gene_vectors.npy` [6885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6885 or target_col == 6885). Every well: [[ACKR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACKR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
