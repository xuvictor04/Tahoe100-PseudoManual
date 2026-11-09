---
symbol: "FSIP2"
type: "gene"
col: 12045
ensembl_id: "ENSG00000188738"
name: "fibrous sheath interacting protein 2"
location: "2q32.1"
module: 9
arm: "+"
pooled_cpm: 8.02
n_lines_expressing: 24
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# FSIP2

*fibrous sheath interacting protein 2* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.29× (z +11.6, q 3e-28, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +5.9, q 7e-07, up in 0 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.607× (z -5.1, q 2e-04, down in 11 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H1573 0.116×, NCI-H2030 0.144×, NCI-H1792 0.239×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.112×, NCI-H1792 0.149×, NCI-H1573 0.258×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (HT-29 0.0744×, LS 180 0.0963×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HCT15 0.0436×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (HT-29 0.126×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR2052HG]] (+0.57, fdr 1e-05), [[AGA-DT]] (+0.57, fdr 3e-05), [[RP1]] (+0.53, fdr 4e-05); moves opposite to [[TMEM231]] (-0.59, fdr 4e-05), [[SFXN2]] (-0.51, fdr 5e-05), [[PRMT7]] (-0.49, fdr 8e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC01426]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +11.6 | 3e-28 | 3/9 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +9.5 | 7e-19 | 4/13 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +8.4 | 8e-15 | 2/11 (CFPAC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.9 | 7e-07 | 0/19 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.004 | 8/20 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.004 | 3/18 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.004 | 7/19 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.13 | 5/18 (BT-474, SW 900, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.36× | +3.1 | 0.13 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.14 | 6/17 (LS 180, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12045.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H1573 0.116×, NCI-H2030 0.144×, NCI-H1792 0.239×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.112×, NCI-H1792 0.149×, NCI-H1573 0.258×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (HT-29 0.0744×, LS 180 0.0963×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HCT15 0.0436×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (HT-29 0.126×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -5.1 | 2e-04 | 11/19 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.616×** | -4.9 | 3e-04 | 11/19 (HCT15, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.687×** | -3.8 | 0.032 | 6/17 (NCI-H23, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.698×** | -3.6 | 0.039 | 10/19 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.720×** | -3.3 | 0.098 | 11/20 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.735× | -3.1 | 0.17 | 2/21 (AN3 CA, NCI-H661) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.741× | -3.0 | 0.19 | 11/21 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | 0.735× | -3.0 | 0.19 | 6/19 (HCT15, MIA PaCa-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 43.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 76.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -16.5) |
| [[HT-29 (line)]] | alt | 8.05 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0744× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.126× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 64.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -11.4) |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0436× (z -10.7) |
| [[LS 180 (line)]] | wt | 8.47 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0963× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -9.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.90 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR2052HG]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[AGA-DT]] | +0.57 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[RP1]] | +0.53 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[LINC00648]] | +0.53 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[CDH8]] | +0.52 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[DMD]] | +0.52 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[LINC01725]] | +0.52 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[DYNLRB2-AS1]] | +0.51 | +0.41 / +0.37 | both halves | 8e-05 |  |
| [[LINC02405]] | +0.51 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[CTNNA3]] | +0.51 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[LINC01905]] | +0.51 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[LINC01807]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM231]] | -0.59 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SFXN2]] | -0.51 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[PRMT7]] | -0.49 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[ARMC10]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TCTN3]] | -0.49 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SFI1]] | -0.48 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[RAB40B]] | -0.48 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[LSM11]] | -0.47 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[MAX]] | -0.46 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[PIGN]] | -0.46 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[FBXO31]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SH2B2]] | -0.45 | -0.24 / -0.43 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FSIP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02405]] | C | LINC02405 activity raises FSIP2's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without LINC02405 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360; co-absent with the target |
| [[PEX5L]] | C | PEX5L activity raises FSIP2's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.00× lower at baseline in the lines without PEX5L | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01426]] | B | FSIP2 activity raises LINC01426's level | lines that do not express FSIP2 (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without FSIP2 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000286797, NPFFR2, GRIA2; maybe low, not absent |
| [[FAM227B]] | B | FSIP2 activity raises FAM227B's level | lines that do not express FSIP2 (26) vs lines expressing it (24) | 1.28× lower at baseline in the lines without FSIP2 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000286797, NPFFR2, GRIA2; maybe low, not absent |
| [[LINC02405]] | C | FSIP2 activity raises LINC02405's level | lines that do not express FSIP2 (26) vs lines expressing it (24) | 2.41× lower at baseline in the lines without FSIP2 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000286797, NPFFR2, GRIA2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.414). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.4, 39.0); signed map (51.3, 32.5). **Vector** length 39.4, 7.90% of its response variance represented; |z| ≥ 3 in 458 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +0.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.1 | -4.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -0.9 | -3.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.7 | -1.3 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[Tazarotene (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | fibrous sheath interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.1 — chr2:185,738,804-185,833,290 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34780 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5CZC0](https://www.uniprot.org/uniprotkb/Q5CZC0) (Fibrous sheath-interacting protein 2):

> Plays a role in spermatogenesis.

**Summary**, from NCBI Gene [401024](https://www.ncbi.nlm.nih.gov/gene/401024):

> This gene encodes a protein associated with the sperm fibrous sheath. Genes encoding most of the fibrous-sheath associated proteins genes are transcribed only during the postmeiotic period of spermatogenesis. The protein encoded by this gene is specific to spermatogenic cells. Copy number variation in this gene may be associated with testicular germ cell tumors. Pseudogenes associated with this gene are reported on chromosomes 2 and X. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:21675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21675) · Entrez [401024](https://www.ncbi.nlm.nih.gov/gene/401024) · UniProt [Q5CZC0](https://www.uniprot.org/uniprotkb/Q5CZC0) · Ensembl [ENSG00000188738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188738)

## Data

Gene col 12045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12045); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12045]; `tensor/DDL_lfc|DDL_z.npy` [12045]; `embed/gene_vectors.npy` [12045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12045 or target_col == 12045). Every well: [[FSIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
