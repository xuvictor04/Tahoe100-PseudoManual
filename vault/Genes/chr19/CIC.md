---
symbol: "CIC"
type: "gene"
col: 1256
ensembl_id: "ENSG00000079432"
name: "capicua transcriptional repressor"
location: "19q13.2"
module: 96
arm: "+"
pooled_cpm: 28.7
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# CIC

*capicua transcriptional repressor* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.32× (z +12.3, q 4e-32, up in 45 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +11.4, q 7e-28, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.786× (z -4.4, q 0.003, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (hTERT-HPNE 0.0771×, A549 0.237×, LoVo 0.234×, HOP62 0.312×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (MIA PaCa-2 0.209×, NCI-H2030 0.251×, NCI-H460 0.314×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.0927×; ⚠ toxic; cell-cycle shift, explains ~21% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.364×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAF1]] (+0.69, fdr 7e-06), [[ZNF687]] (+0.67, fdr 7e-06), [[CELSR3]] (+0.67, fdr 7e-06); moves opposite to [[NME2]] (-0.55, fdr 6e-05), [[GCSH]] (-0.53, fdr 4e-05), [[PALS2]] (-0.52, fdr 4e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRIP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.32×** | +12.3 | 4e-32 | 45/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +11.4 | 7e-28 | 39/47 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +5.4 | 1e-05 | 31/48 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.004 | 25/47 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +3.8 | 0.020 | 20/48 (A498, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.049 | 18/47 (NCI-H2030, SW480, …) | two highest doses | low cells (technical?); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.4 | 0.063 | 20/45 (HEC-1-A, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1256.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (hTERT-HPNE 0.0771×, A549 0.237×, LoVo 0.234×, HOP62 0.312×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (MIA PaCa-2 0.209×, NCI-H2030 0.251×, NCI-H460 0.314×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.0927×; ⚠ toxic; cell-cycle shift, explains ~21% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.364×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.786×** | -4.4 | 0.003 | 24/48 (HT-29, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -4.4 | 0.003 | 22/46 (RPMI-7951, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.736×** | -4.0 | 0.012 | 22/48 (C32, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.755×** | -3.7 | 0.037 | 22/48 (SW 900, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -3.5 | 0.037 | 24/48 (MIA PaCa-2, HOP62, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.755×** | -3.5 | 0.037 | 17/33 (hTERT-HPNE, A549, …) | rises with dose | composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.764×** | -3.5 | 0.037 | 19/48 (BT-474, HT-29, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.772×** | -3.2 | 0.085 | 17/46 (H4, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | 0.788× | -3.1 | 0.12 | 19/48 (SK-MEL-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.790× | -3.1 | 0.12 | 16/46 (HOP62, RPMI-7951, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 31.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +15.8) | — |
| [[A549 (line)]] | wt | 48.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 29.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.65× (z +11.7) ⚠ position not correctable | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[NCI-H460 (line)]] | wt | 24.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[HepG2_C3A (line)]] | wt | 28.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.4) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.199× (z -9.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 17.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H2030 (line)]] | alt | 25.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[PANC-1 (line)]] | alt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +14.4) | — |
| [[A-427 (line)]] | wt | 24.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.364× (z -9.7) |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[H4 (line)]] | wt | 43.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0927× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[HOP62 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HS-578T (line)]] | alt | 35.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0771× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LS 180 (line)]] | wt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0891× (z -8.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.7) | — |
| [[A-172 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAF1]] | +0.69 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[ZNF687]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CELSR3]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PRR14]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ZNF574]] | +0.62 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[ZNF646]] | +0.62 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[PLXNB2]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TFE3]] | +0.60 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[RELA]] | +0.59 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[KHNYN]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DXO]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME2]] | -0.55 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[GCSH]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[PALS2]] | -0.52 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[EEF1E1]] | -0.51 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[LINC03006-1]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[UBE3D]] | -0.50 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[LDHB]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[LYPLA1]] | -0.49 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[CNIH1]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIP6]] | B | TRIP6 activity raises CIC's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.43× lower at baseline in the lines without TRIP6 | 0.012 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.9, 4.2); signed map (11.2, -17.9). **Vector** length 112, 28.3% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +11.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +6.3 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | -1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.7 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +0.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +2.4 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.1 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.7 | -2.9 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.4 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -3.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.9 | -2.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.8 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | capicua transcriptional repressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:42,268,537-42,295,797 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0306 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RK0](https://www.uniprot.org/uniprotkb/Q96RK0) (Protein capicua homolog):

> Transcriptional repressor which plays a role in development of the central nervous system (CNS). In concert with ATXN1 and ATXN1L, involved in brain development.

**Summary**, from NCBI Gene [23152](https://www.ncbi.nlm.nih.gov/gene/23152):

> The protein encoded by this gene is an ortholog of the Drosophila melanogaster capicua gene, and is a member of the high mobility group (HMG)-box superfamily of transcriptional repressors. This protein contains a conserved HMG domain that is involved in DNA binding and nuclear localization, and a conserved C-terminus. Studies suggest that the N-terminal region of this protein interacts with Atxn1 (GeneID:6310), to form a transcription repressor complex, and in vitro studies suggest that …

**Accessions** — [HGNC:14214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14214) · Entrez [23152](https://www.ncbi.nlm.nih.gov/gene/23152) · UniProt [Q96RK0](https://www.uniprot.org/uniprotkb/Q96RK0) · Ensembl [ENSG00000079432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079432)

## Data

Gene col 1256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1256); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1256]; `tensor/DDL_lfc|DDL_z.npy` [1256]; `embed/gene_vectors.npy` [1256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1256 or target_col == 1256). Every well: [[CIC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
