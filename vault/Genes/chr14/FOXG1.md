---
symbol: "FOXG1"
type: "gene"
col: 10690
ensembl_id: "ENSG00000176165"
name: "forkhead box G1"
location: "14q12"
module: 154
arm: "+"
pooled_cpm: 3.02
n_lines_expressing: 14
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# FOXG1

*forkhead box G1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.99× (z +11.9, q 4e-30, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.28× (z +11.6, q 7e-29, up in 9 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM: 0.547× (z -3.9, q 0.054, down in 1 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW480 0.170×, NCI-H661 0.224×; ⚠ cell-cycle shift, explains ~0% of this change); [[Simotinib (drug)]] 5 µM in 1 line (A-427 0.0878×; ⚠ toxic).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01551]] (+0.72, fdr 7e-06, ⚠ same locus), [[TMX4]] (+0.61, fdr 1e-04), [[SOCS6]] (+0.59, fdr 4e-05), [[RNF146]] (+0.58, fdr 3e-04); moves opposite to [[ADAMTS16]] (-0.62, fdr 6e-05), [[ATG16L2]] (-0.55, fdr 4e-04), [[EFL1]] (-0.55, fdr 3e-04).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ARID3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.99×** | +11.9 | 4e-30 | 5/6 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +11.6 | 7e-29 | 9/10 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.64×** | +10.7 | 3e-24 | 6/7 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.24×** | +9.3 | 3e-18 | 6/7 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +7.0 | 4e-10 | 5/10 (H4, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.44×** | +6.1 | 9e-08 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.30×** | +5.8 | 7e-07 | 1/9 (LOX-IMVI) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +5.5 | 3e-06 | 6/9 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +5.4 | 3e-06 | 3/9 (HOP62, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +5.4 | 3e-06 | 3/9 (LOX-IMVI, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.65×** | +4.8 | 8e-05 | 1/9 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +4.4 | 5e-04 | 6/9 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +4.4 | 5e-04 | 1/11 (A-427) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.56×** | +4.4 | 5e-04 | 5/9 (NCI-H1792, LOX-IMVI, …) | top dose only | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.25×** | +4.0 | 0.002 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.014 | 3/11 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.65×** | +3.5 | 0.017 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.017 | 6/10 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.63×** | +3.4 | 0.019 | 0/10 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.019 | 3/11 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.67×** | +3.3 | 0.024 | 0/10 | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.64×** | +3.2 | 0.032 | 1/9 (HOP62) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.53×** | +2.9 | 0.065 | 3/10 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.51×** | +2.8 | 0.091 | 1/10 (HOP62) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10690.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW480 0.170×, NCI-H661 0.224×; ⚠ cell-cycle shift, explains ~0% of this change); [[Simotinib (drug)]] 5 µM in 1 line (A-427 0.0878×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | **0.547×** | -3.9 | 0.054 | 1/10 (H4) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.871× | -3.5 | 0.13 | 3/12 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | 0.634× | -3.1 | 0.32 | 2/10 (HOP62, HEC-1-A) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 9.41 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.5) | — |
| [[SW480 (line)]] | alt | 7.82 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 6.10 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0878× (z -9.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +8.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H661 (line)]] | alt | 258 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.265 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.769 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.326 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01551]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TMX4]] | +0.61 | +0.50 / +0.33 | both halves | 1e-04 |  |
| [[SOCS6]] | +0.59 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[RNF146]] | +0.58 | +0.50 / +0.29 | both halves | 3e-04 |  |
| [[RDX]] | +0.55 | +0.55 / +0.37 | both halves | 9e-05 |  |
| [[YAP1]] | +0.55 | +0.37 / +0.36 | both halves | 1e-04 |  |
| [[TRIM7]] | +0.55 | +0.32 / +0.34 | both halves | 2e-04 |  |
| [[MBNL1]] | +0.54 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[STXBP5-AS1]] | +0.54 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[SLC7A2]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[LINC01170]] | +0.53 | +0.47 / +0.31 | both halves | 2e-04 |  |
| [[UTRN]] | +0.53 | +0.48 / +0.33 | both halves | 1e-04 |  |
| [[RIPOR2]] | +0.52 | +0.44 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS16]] | -0.62 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[ATG16L2]] | -0.55 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[EFL1]] | -0.55 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[MYO9B]] | -0.55 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[ARID5A]] | -0.54 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[WSCD1]] | -0.53 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[ARID3B]] | -0.53 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[PLAUR]] | -0.53 | -0.51 / -0.23 | both halves | 5e-04 |  |
| [[UBA6]] | -0.52 | -0.48 / -0.20 | both halves | 7e-04 |  |
| [[RASSF2]] | -0.52 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[GPRIN1]] | -0.51 | -0.36 / -0.24 | both halves | 5e-04 | pathway: Transcriptional Regulation by MECP2 |
| [[CMIP]] | -0.51 | -0.42 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FOXG1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC1A3]] | C | SLC1A3 activity raises FOXG1's level | lines that do not express SLC1A3 (21) vs lines expressing it (29) | 2.02× lower at baseline in the lines without SLC1A3 | 0.077 | ⚠ within organs, on part of the lines; also absent: LRP2, SLIT2, CHSY3; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARID3B]] | B | FOXG1 activity raises ARID3B's level | lines that do not express FOXG1 (36) vs lines expressing it (14) | 1.41× lower at baseline in the lines without FOXG1 | 0.094 | ⚠ within organs, on part of the lines; co-absent genes; also absent: LINC02566, MMRN1, GCG |
| [[ADAMTS18]] | C | FOXG1 activity raises ADAMTS18's level | lines that do not express FOXG1 (36) vs lines expressing it (14) | 2.19× lower at baseline in the lines without FOXG1 | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; also absent: LINC02566, MMRN1, GCG; co-absent with the target |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction -0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, 16.8); signed map (25.5, -18.9). **Vector** length 28.0, 7.06% of its response variance represented; |z| ≥ 3 in 240 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +5.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +0.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.0 | +0.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.9 | -0.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.3 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.6 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.6 | -1.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.4 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box G1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:28,764,329-28,770,277 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HFK2, QIN, BF1, HFK1, HFK3, HBF-3; previously FKHL2, FOXG1B, FKHL4, FKH2, FKHL1 |
| Gene groups (HGNC) | Forkhead boxes |
| Reactome | 4 pathways, smallest: FOXO-mediated transcription of cell cycle genes; Regulation of MECP2 expression and activity; Transcriptional Regulation by MECP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P55316](https://www.uniprot.org/uniprotkb/P55316) (Forkhead box protein G1):

> Transcription repression factor which plays an important role in the establishment of the regional subdivision of the developing brain and in the development of the telencephalon.

**Summary**, from NCBI Gene [2290](https://www.ncbi.nlm.nih.gov/gene/2290):

> This locus encodes a member of the fork-head transcription factor family. The encoded protein, which functions as a transcriptional repressor, is highly expressed in neural tissues during brain development. Mutations at this locus have been associated with Rett syndrome and a diverse spectrum of neurodevelopmental disorders defined as part of the FOXG1 syndrome. This gene is disregulated in many types of cancer and is the target of multiple microRNAs that regulate the proliferation of tumor …

**Accessions** — [HGNC:3811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3811) · Entrez [2290](https://www.ncbi.nlm.nih.gov/gene/2290) · UniProt [P55316](https://www.uniprot.org/uniprotkb/P55316) · Ensembl [ENSG00000176165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176165)

## Data

Gene col 10690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10690); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10690]; `tensor/DDL_lfc|DDL_z.npy` [10690]; `embed/gene_vectors.npy` [10690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10690 or target_col == 10690). Every well: [[FOXG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
