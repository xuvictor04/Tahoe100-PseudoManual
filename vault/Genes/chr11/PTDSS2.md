---
symbol: "PTDSS2"
type: "gene"
col: 10541
ensembl_id: "ENSG00000174915"
name: "phosphatidylserine synthase 2"
location: "11p15.5"
module: 3
arm: "+"
pooled_cpm: 15.71
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PTDSS2

*phosphatidylserine synthase 2* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.62× (z +9.8, q 8e-20, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 2.70×).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.781× (z -7.1, q 8e-10, down in 25 of 47 measured lines) ⚠ cell-cycle shift, explains ~17% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.722× (z -6.6, q 1e-08, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RILPL1]] (+0.68, fdr 7e-06), [[MARK4]] (+0.65, fdr 1e-05), [[PKD1P6]] (+0.64, fdr 1e-05); moves opposite to [[DCLRE1A]] (-0.60, fdr 8e-06), [[FAM111A]] (-0.58, fdr 1e-05), [[DZIP3]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNTA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10541.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 2.70×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +9.8 | 8e-20 | 30/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.2 | 6e-05 | 14/37 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.6 | 9e-04 | 8/23 (NCI-H2347, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +4.1 | 0.005 | 10/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +4.1 | 0.006 | 12/47 (RPMI-7951, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.024 | 7/44 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.6 | 0.024 | 4/32 (SW1417, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.053 | 12/45 (RPMI-7951, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.059 | 13/46 (SW480, LoVo, …) | top dose only |  |
| [[Silodosin (drug)]] 5 µM |  | 1.18× | +3.1 | 0.097 | 8/46 (SNU-1, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.17× | +3.1 | 0.097 | 12/47 (PANC-1, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.781×** | -7.1 | 8e-10 | 25/47 (A-427, SK-MEL-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.722×** | -6.6 | 1e-08 | 26/47 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.747×** | -5.5 | 6e-06 | 21/46 (LOX-IMVI, SNU-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -3.7 | 0.027 | 19/48 (HEC-1-A, AN3 CA, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.726×** | -3.4 | 0.080 | 4/48 (A-427, NCI-H661, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.856× | -3.1 | 0.16 | 2/48 (NCI-H2347, CFPAC-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 19.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -15.4) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0807× (z -9.5) |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 1 | — | [[Vitamin K4 (drug)]] 0.5 µM 0.0655× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0786× (z -15.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 6.62 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.3) ⚠ cell-cycle shift, explains ~17% of this change |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -10.2) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.2) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SW480 (line)]] | alt | 17.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.70× (z +9.8) | — |
| [[A-172 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RILPL1]] | +0.68 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[MARK4]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[PKD1P6]] | +0.64 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[AGAP3]] | +0.62 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GNPTG]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[FOXK2]] | +0.61 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[STK32C]] | +0.61 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[CORO7]] | +0.61 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[FLYWCH1]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ANKRD13B]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[BRI3]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[POLR2F]] | +0.60 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | -0.60 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[FAM111A]] | -0.58 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.56 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[BCLAF1]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[SUB1]] | -0.55 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[FUNDC1]] | -0.54 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[ZNF620]] | -0.54 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[SPDL1]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[IFT80]] | -0.53 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[ZNF644]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CGGBP1]] | -0.52 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[ZC3H11A]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNTA1]] | B | SNTA1 activity raises PTDSS2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without SNTA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.9, -2.9); signed map (-41.3, 2.4). **Vector** length 64.5, 9.76% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +9.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.5 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +2.5 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.5 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.6 | -7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.9 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylserine synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:448,268-491,399 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PSS2 |
| Reactome | 3 pathways, smallest: Glycerophospholipid biosynthesis; Phospholipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVG9](https://www.uniprot.org/uniprotkb/Q9BVG9) (Phosphatidylserine synthase 2):

> Catalyzes a base-exchange reaction in which the polar head group of phosphatidylethanolamine (PE) is replaced by L-serine to form phosphatidylserine. Lacks phosphatidylcholine-dependent base-exchange activity. Can utilize both phosphatidylethanolamine (PE) plasmalogen and diacyl PE as substrate and the latter is six times better utilized, indicating the importance of an ester linkage at the sn-1 position (By similarity). Although it shows no sn-1 fatty acyl preference, exhibits significant …

**Summary**, from NCBI Gene [81490](https://www.ncbi.nlm.nih.gov/gene/81490):

> The protein encoded by this gene catalyzes the conversion of phosphatidylethanolamine to phosphatidylserine, a structural membrane phospholipid that functions in cell signaling, blood coagulation, and apoptosis. The encoded enzyme also has a high affinity for docosahexaenoic acid (DHA) and can use it to make DHA-containing phosphatidylserine. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:15463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15463) · Entrez [81490](https://www.ncbi.nlm.nih.gov/gene/81490) · UniProt [Q9BVG9](https://www.uniprot.org/uniprotkb/Q9BVG9) · Ensembl [ENSG00000174915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174915)

## Data

Gene col 10541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10541); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10541]; `tensor/DDL_lfc|DDL_z.npy` [10541]; `embed/gene_vectors.npy` [10541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10541 or target_col == 10541). Every well: [[PTDSS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTDSS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
