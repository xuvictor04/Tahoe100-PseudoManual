---
symbol: "TRMT61B"
type: "gene"
col: 10050
ensembl_id: "ENSG00000171103"
name: "tRNA methyltransferase 61B"
location: "2p23.2"
module: 1
arm: "+"
pooled_cpm: 17.56
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TRMT61B

*tRNA methyltransferase 61B* — 2p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.30× (z +5.9, q 2e-06, up in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.41× (z +5.5, q 1e-05, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.579× (z -8.7, q 1e-15, down in 25 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 0.529× (z -5.3, q 2e-05, down in 22 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.115×, KATO III 0.204×, RPMI-7951 0.149×, Hs 766T 0.191×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.158×, NCI-H23 0.211×, C-33 A 0.170×, SK-MEL-2 0.221×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-172 0.135×, NCI-H23 0.189×, HEC-1-A 0.295×; ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (BT-474 0.0902×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (COLO 205 0.0872×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (A-172 0.253×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UMPS]] (+0.76, fdr 7e-06), [[PAAF1]] (+0.69, fdr 7e-06), [[TMLHE]] (+0.68, fdr 1e-05); moves opposite to [[CCNYL1]] (-0.59, fdr 1e-05), [[HAP1]] (-0.57, fdr 1e-05), [[EPB41L5]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GALNT16]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10050.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.30×** | +5.9 | 2e-06 | 26/48 (NCI-H1573, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +5.5 | 1e-05 | 22/47 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.37×** | +4.9 | 2e-04 | 15/44 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +4.8 | 3e-04 | 19/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.33×** | +4.6 | 4e-04 | 14/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.005 | 14/48 (A498, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.18× | +3.7 | 0.016 | 16/47 (A549, LS 180, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.022 | 11/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.24×** | +3.5 | 0.025 | 15/48 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.033 | 12/47 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.033 | 7/48 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.091 | 3/47 (SNU-423, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10050.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.115×, KATO III 0.204×, RPMI-7951 0.149×, Hs 766T 0.191×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.158×, NCI-H23 0.211×, C-33 A 0.170×, SK-MEL-2 0.221×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-172 0.135×, NCI-H23 0.189×, HEC-1-A 0.295×; ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (BT-474 0.0902×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (COLO 205 0.0872×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (A-172 0.253×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.579×** | -8.7 | 1e-15 | 25/43 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.642×** | -6.8 | 3e-09 | 15/30 (NCI-H460, KATO III, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.529×** | -5.3 | 2e-05 | 22/45 (HOP62, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -4.7 | 4e-04 | 17/48 (A498, SW 900, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.751×** | -4.4 | 0.001 | 18/46 (SNU-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -4.3 | 0.001 | 4/48 (Hs 766T, AN3 CA, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.805×** | -3.5 | 0.044 | 10/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.815×** | -3.3 | 0.079 | 14/48 (SW 900, SHP-77, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | 0.824× | -3.1 | 0.13 | 15/46 (AsPC-1, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.253× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 32.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 19.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -17.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -14.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 7.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0946× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0902× (z -10.9) |
| [[C-33 A (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -10.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0872× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.139× (z -8.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -9.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -10.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -9.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -10.1) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A498 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UMPS]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[PAAF1]] | +0.69 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[TMLHE]] | +0.68 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[PALB2]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[QTRT2]] | +0.65 | +0.57 / +0.64 | both halves | 9e-06 | pathway: tRNA processing; STRING 496 |
| [[DNAJC17]] | +0.65 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[MRRF]] | +0.64 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[POLR3F]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 | STRING 452 |
| [[GTPBP10]] | +0.63 | +0.68 / +0.52 | both halves | 1e-05 | STRING 473 |
| [[QRSL1]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ALKBH3]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 | STRING 677 |
| [[GATB]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL1]] | -0.59 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[HAP1]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[EPB41L5]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[HYCC1]] | -0.54 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT16]] | B | GALNT16 activity raises TRMT61B's level | lines that do not express GALNT16 (8) vs lines expressing it (42) | 1.34× lower at baseline in the lines without GALNT16 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000237356, PRKAR2B, FRG1-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-44.8, 7.6); signed map (-9.5, -17.3). **Vector** length 66.9, 10.5% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +3.8 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.9 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +0.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -4.7 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.2 | -8.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | +0.9 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | +0.5 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.3 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 61B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.2 — chr2:28,849,821-28,870,309 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20628 |
| Gene groups (HGNC) | 7BS N1-adenosine RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 4 pathways, smallest: tRNA modification in the mitochondrion; Mitochondrial mRNA modification; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVS5](https://www.uniprot.org/uniprotkb/Q9BVS5) (tRNA):

> Methyltransferase that catalyzes the formation of N(1)-methyladenine at position 58 (m1A58) in various tRNAs in mitochondrion, including tRNA(Leu) (deciphering codons UUA or UUG), tRNA(Lys) and tRNA(Ser) (deciphering codons UCA, UCU, UCG or UCC). Catalyzes the formation of 1-methyladenosine at position 947 of mitochondrial 16S ribosomal RNA and this modification is most likely important for mitoribosomal structure and function. In addition to tRNA N(1)-methyltransferase activity, also acts as a …

**Summary**, from NCBI Gene [55006](https://www.ncbi.nlm.nih.gov/gene/55006):

> Enables mRNA (adenine-N1-)-methyltransferase activity; rRNA (adenine) methyltransferase activity; and tRNA (adenine(58)-N1)-methyltransferase activity. Involved in mRNA processing and mitochondrial tRNA processing. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26070) · Entrez [55006](https://www.ncbi.nlm.nih.gov/gene/55006) · UniProt [Q9BVS5](https://www.uniprot.org/uniprotkb/Q9BVS5) · Ensembl [ENSG00000171103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171103)

## Data

Gene col 10050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10050); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10050]; `tensor/DDL_lfc|DDL_z.npy` [10050]; `embed/gene_vectors.npy` [10050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10050 or target_col == 10050). Every well: [[TRMT61B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT61B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
