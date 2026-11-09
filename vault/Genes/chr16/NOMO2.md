---
symbol: "NOMO2"
type: "gene"
col: 11634
ensembl_id: "ENSG00000185164"
name: "NODAL modulator 2"
location: "16p12.3"
module: 42
arm: "+"
pooled_cpm: 7.91
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# NOMO2

*NODAL modulator 2* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.19× (z +8.0, q 8e-13, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.583× (z -5.3, q 8e-05, down in 21 of 46 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.694× (z -3.7, q 0.039, down in 14 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STT3A]] (+0.79, fdr 7e-06), [[NOMO3]] (+0.79, fdr 7e-06), [[MSTO2P]] (+0.76, fdr 7e-06); moves opposite to [[EIF4EBP3]] (-0.66, fdr 7e-06), [[LINC02307]] (-0.65, fdr 1e-05), [[TRIM47]] (-0.63, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TBX3]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Selinexor (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +8.0 | 8e-13 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +7.8 | 1e-12 | 41/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +7.0 | 4e-10 | 34/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +4.5 | 0.001 | 16/41 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +4.3 | 0.002 | 12/47 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +3.7 | 0.023 | 11/48 (hTERT-HPNE, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.071 | 11/43 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | 1.80× | +3.1 | 0.12 | 1/45 (PANC-1) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.583×** | -5.3 | 8e-05 | 21/46 (J82, A549, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -4.4 | 0.003 | 15/48 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -3.7 | 0.039 | 14/46 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.708×** | -3.5 | 0.065 | 14/45 (RKO, A-427, …) | top dose only |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | **0.789×** | -3.4 | 0.073 | 12/48 (CHP-212, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.794×** | -3.3 | 0.086 | 20/45 (A-172, NCI-H2030, …) | rises with dose | composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 12.1 | 0 | 2 | — | [[Naproxen (drug)]] 5 µM 0.0825× (z -9.4) |
| [[A-172 (line)]] | wt | 9.59 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 7.29 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0552× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -9.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 6.97 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0662× (z -10.5) ⚠ cell-cycle shift, explains ~11% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.80 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.0856× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 6.77 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0755× (z -11.3) |
| [[SHP-77 (line)]] | alt | 8.10 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.0817× (z -9.7) |
| [[A-427 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3A]] | +0.79 | +0.80 / +0.80 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[NOMO3]] | +0.79 | +0.67 / +0.77 | both halves | 7e-06 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[MSTO2P]] | +0.76 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[ALDH18A1]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.70 | +0.75 / +0.63 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[SEC24C]] | +0.70 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[PDIA4]] | +0.70 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[TMED2]] | +0.70 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[GGCX]] | +0.69 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[TXNDC5]] | +0.69 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[INTS11]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SEPTIN7P14]] | +0.69 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4EBP3]] | -0.66 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[LINC02307]] | -0.65 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[TRIM47]] | -0.63 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.63 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[ZBED1]] | -0.62 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[PBDC1]] | -0.62 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ANKRD26]] | -0.61 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[KANSL1L]] | -0.61 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ZNF518A]] | -0.60 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[RSF1]] | -0.59 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[PNRC1]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.59 | -0.59 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX3]] | B | TBX3 activity raises NOMO2's level | lines that do not express TBX3 (10) vs lines expressing it (40) | 1.24× lower at baseline in the lines without TBX3 | 0.053 | ⚠ within organs, on part of the lines |
| [[HDAC6]] | B | HDAC6 activity lowers NOMO2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[POGLUT2]] | C | POGLUT2 activity raises NOMO2's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Selinexor (drug)]] 0.5 µM | C | NOMO2's natural level raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | NOMO2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.291 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.5, -28.6); signed map (-54.5, 2.7). **Vector** length 65.0, 9.99% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.57 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.56 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.55 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +8.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.3 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | NODAL modulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:18,417,325-18,562,211 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOMO, PM5 |
| Gene groups (HGNC) | BOS complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JPE7](https://www.uniprot.org/uniprotkb/Q5JPE7) (BOS complex subunit NOMO2):

> Component of the multi-pass translocon (MPT) complex that mediates insertion of multi-pass membrane proteins into the lipid bilayer of membranes. The MPT complex takes over after the SEC61 complex: following membrane insertion of the first few transmembrane segments of proteins by the SEC61 complex, the MPT complex occludes the lateral gate of the SEC61 complex to promote insertion of subsequent transmembrane regions.

**Summary**, from NCBI Gene [283820](https://www.ncbi.nlm.nih.gov/gene/283820):

> This gene encodes a protein originally thought to be related to the collagenase gene family. This gene is one of three highly similar genes in a region of duplication located on the p arm of chromosome 16. These three genes encode closely related proteins that may have the same function. The protein encoded by one of these genes has been identified as part of a protein complex that participates in the Nodal signaling pathway during vertebrate development. Mutations in ABCC6, which is located …

**Accessions** — [HGNC:22652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22652) · Entrez [283820](https://www.ncbi.nlm.nih.gov/gene/283820) · UniProt [Q5JPE7](https://www.uniprot.org/uniprotkb/Q5JPE7) · Ensembl [ENSG00000185164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185164)

## Data

Gene col 11634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11634); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11634]; `tensor/DDL_lfc|DDL_z.npy` [11634]; `embed/gene_vectors.npy` [11634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11634 or target_col == 11634). Every well: [[NOMO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOMO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
