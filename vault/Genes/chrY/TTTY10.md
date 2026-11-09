---
symbol: "TTTY10"
type: "gene"
col: 13698
ensembl_id: "ENSG00000229236"
name: "testis expressed transcript, Y-linked 10"
location: "Yq11.223"
module: 19
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 19
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 13
direction_downstream: 23
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# TTTY10

*testis expressed transcript, Y-linked 10* — Yq11.223

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.56× (z +10.2, q 7e-22, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +5.4, q 9e-06, up in 9 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.500× (z -5.1, q 2e-04, down in 14 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 0.0782×, HepG2/C3A 0.0634×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 2 lines (COLO 205 0.0579×, HepG2/C3A 0.101×; ⚠ cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.111×; ⚠ cell-cycle shift, would explain all of this change); [[Methotrexate (drug)]] 0.5 µM in 1 line (COLO 205 0.0633×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (H4 0.0506×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHL1]] (+0.61, fdr 3e-05), [[SOX6]] (+0.59, fdr 1e-05), [[GREM2]] (+0.58, fdr 3e-05); moves opposite to [[CASP9]] (-0.42, fdr 4e-04), [[EML6]] (-0.40, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TXLNGY]], [[TXLNGY-1]] → it (grade C ⚠); 23 go from it, the strongest it → [[SLCO1C1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13698.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.56×** | +10.2 | 7e-22 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +7.1 | 4e-10 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +7.0 | 7e-10 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.4 | 9e-06 | 9/14 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.64×** | +5.1 | 3e-05 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +4.0 | 0.007 | 4/14 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.66×** | +3.8 | 0.014 | 4/14 (LoVo, A-172, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.98×** | +3.6 | 0.023 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.40×** | +3.5 | 0.024 | 1/16 (NCI-H460) | top dose only | low cells (technical?) |
| [[Ataluren (drug)]] 0.5 µM |  | **1.61×** | +3.5 | 0.024 | 4/15 (hTERT-HPNE, LoVo, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.91×** | +3.4 | 0.034 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.56×** | +3.3 | 0.047 | 1/13 (H4) | inconsistent across doses | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.72×** | +3.2 | 0.051 | 1/14 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.18× | +3.0 | 0.10 | 0/4 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13698.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 0.0782×, HepG2/C3A 0.0634×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 2 lines (COLO 205 0.0579×, HepG2/C3A 0.101×; ⚠ cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.111×; ⚠ cell-cycle shift, would explain all of this change); [[Methotrexate (drug)]] 0.5 µM in 1 line (COLO 205 0.0633×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (H4 0.0506×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.500×** | -5.1 | 2e-04 | 14/15 (H4, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.573×** | -4.1 | 0.010 | 11/17 (HepG2/C3A, H4, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.589×** | -3.9 | 0.017 | 9/15 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.621×** | -3.5 | 0.058 | 1/15 (SK-MEL-2) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.628×** | -3.4 | 0.064 | 10/15 (COLO 205, HepG2/C3A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.580× | -3.3 | 0.11 | 9/16 (NCI-H460, A-427, …) | top dose only | composition shift; noisy plate (z scaled) |
| [[Malotilate (drug)]] 0.5 µM |  | 0.660× | -3.1 | 0.17 | 6/16 (SK-MEL-2, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0323× (z -12.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[COLO 205 (line)]] | alt | 7.46 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0579× (z -9.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Methotrexate (drug)]] 0.5 µM 0.0633× (z -8.9) |
| [[C32 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 11.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0506× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 8.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0782× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.230 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.232 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHL1]] | +0.61 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[SOX6]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[GREM2]] | +0.58 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[FENDRR]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 | same gene group |
| [[KCNK2]] | +0.58 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[LINC02008]] | +0.57 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[FBXL7]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ACSS3]] | +0.55 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[EDNRB]] | +0.55 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[LINC00824]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[GASK1B-AS1]] | +0.52 | +0.61 / +0.27 | both halves | 3e-04 |  |
| [[TTTY14]] | +0.51 | +0.60 / +0.42 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP9]] | -0.42 | -0.39 / -0.25 | both halves | 4e-04 |  |
| [[EML6]] | -0.40 | -0.34 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TXLNGY]], [[TXLNGY-1]] | C | TXLNGY, TXLNGY-1 activity raises TTTY10's level | lines that do not express TXLNGY, TXLNGY-1 (30) vs lines expressing them (20) | 5.93× lower at baseline in the lines without TXLNGY, TXLNGY-1 | 8e-06 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target; co-absent genes |
| [[TTTY14]] | C | TTTY14 activity raises TTTY10's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 4.41× lower at baseline in the lines without TTTY14 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |
| [[UTY]] | C | UTY activity raises TTTY10's level | lines that do not express UTY (31) vs lines expressing it (19) | 5.34× lower at baseline in the lines without UTY | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[LINC00278]] | C | LINC00278 activity raises TTTY10's level | lines that do not express LINC00278 (32) vs lines expressing it (18) | 3.71× lower at baseline in the lines without LINC00278 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, RPS4Y1; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises TTTY10's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 4.32× lower at baseline in the lines without NLGN4Y | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[LIN7A]] | C | LIN7A activity raises TTTY10's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 3.28× lower at baseline in the lines without LIN7A | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises TTTY10's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 3.20× lower at baseline in the lines without CHL1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises TTTY10's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.57× lower at baseline in the lines without LOXL3 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises TTTY10's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.33× lower at baseline in the lines without LINC03000 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises TTTY10's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.05× lower at baseline in the lines without MIR99AHG | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[CDH19]] | C | CDH19 activity raises TTTY10's level | lines that do not express CDH19 (40) vs lines expressing it (10) | 1.89× lower at baseline in the lines without CDH19 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, TBXT, LINC01425; co-absent with the target |
| [[TNFRSF19]] | C | TNFRSF19 activity raises TTTY10's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without TNFRSF19 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 4, C 19. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO1C1]] | B | TTTY10 activity raises SLCO1C1's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 1.65× lower at baseline in the lines without TTTY10 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY |
| [[LINC02398]] | B | TTTY10 activity raises LINC02398's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 2.36× lower at baseline in the lines without TTTY10 | 0.011 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY |
| [[KCNK2]] | B | TTTY10 activity raises KCNK2's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without TTTY10 | 0.052 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY |
| [[SOX6]] | B | TTTY10 activity raises SOX6's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without TTTY10 | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY |
| [[TXLNGY]] | C | TTTY10 activity raises TXLNGY's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 14.61× lower at baseline in the lines without TTTY10 | 7e-07 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[TXLNGY-1]] | C | TTTY10 activity raises TXLNGY-1's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 9.78× lower at baseline in the lines without TTTY10 | 9e-07 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[UTY]] | C | TTTY10 activity raises UTY's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 21.86× lower at baseline in the lines without TTTY10 | 2e-05 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[TTTY14]] | C | TTTY10 activity raises TTTY14's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 5.88× lower at baseline in the lines without TTTY10 | 4e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[NLGN4Y]] | C | TTTY10 activity raises NLGN4Y's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 6.41× lower at baseline in the lines without TTTY10 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[PDE3A]] | C | TTTY10 activity raises PDE3A's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 3.00× lower at baseline in the lines without TTTY10 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[CDH19]] | C | TTTY10 activity raises CDH19's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 2.70× lower at baseline in the lines without TTTY10 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[MIR99AHG]] | C | TTTY10 activity raises MIR99AHG's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 3.47× lower at baseline in the lines without TTTY10 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.3, 35.8); signed map (42.1, 41.5). **Vector** length 36.6, 8.50% of its response variance represented; |z| ≥ 3 in 385 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +10.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | -0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.9 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.8 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.8 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -0.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.0 | -0.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -0.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed transcript, Y-linked 10 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Yq11.223 — chrY:20,464,916-20,575,519 (-) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00133, lnc-KDM5D-4 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

UniProt [Q9BZA0](https://www.uniprot.org/uniprotkb/Q9BZA0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:18491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18491) · Entrez [246119](https://www.ncbi.nlm.nih.gov/gene/246119) · UniProt [Q9BZA0](https://www.uniprot.org/uniprotkb/Q9BZA0) · Ensembl [ENSG00000229236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229236)

## Data

Gene col 13698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13698); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13698]; `tensor/DDL_lfc|DDL_z.npy` [13698]; `embed/gene_vectors.npy` [13698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13698 or target_col == 13698). Every well: [[TTTY10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTTY10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
