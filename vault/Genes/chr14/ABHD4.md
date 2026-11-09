---
symbol: "ABHD4"
type: "gene"
col: 1962
ensembl_id: "ENSG00000100439"
name: "abhydrolase domain containing 4, N-acyl phospholipase B"
location: "14q11.2"
module: 171
arm: "+"
pooled_cpm: 12.49
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# ABHD4

*abhydrolase domain containing 4, N-acyl phospholipase B* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.98× (z +10.3, q 3e-22, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.553× (z -5.9, q 3e-06, down in 28 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.441× (z -4.3, q 0.002, down in 22 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO7]] (+0.60, fdr 1e-05), [[GABARAPL1]] (+0.59, fdr 1e-05), [[HSD17B7P2]] (+0.59, fdr 1e-05); moves opposite to [[PFN1]] (-0.60, fdr 3e-05), [[SNRPB]] (-0.56, fdr 1e-05), [[POLR1G]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LURAP1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.98×** | +10.3 | 3e-22 | 40/45 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.62×** | +9.7 | 1e-19 | 40/46 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.47×** | +9.1 | 2e-17 | 40/46 (COLO 205, HEC-1-A, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.66×** | +5.1 | 5e-05 | 28/46 (J82, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +4.7 | 3e-04 | 22/46 (C32, BT-474, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.23×** | +4.2 | 0.002 | 21/45 (HEC-1-A, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.34×** | +4.1 | 0.003 | 18/47 (RKO, LOX-IMVI, …) | top dose only | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.33×** | +4.0 | 0.005 | 15/47 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.44×** | +3.8 | 0.009 | 11/47 (HEC-1-A, AsPC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.70×** | +3.8 | 0.009 | 14/47 (HOP62, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.010 | 18/45 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.010 | 16/46 (A498, RKO, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.45×** | +3.5 | 0.022 | 15/45 (A498, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.025 | 13/46 (Hs 766T, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.88×** | +3.3 | 0.037 | 12/43 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.042 | 15/47 (NCI-H2030, Hs 766T, …) | all doses, flat | position effect removed |
| [[Alpelisib (drug)]] 5 µM |  | **1.81×** | +3.1 | 0.065 | 9/40 (HEC-1-A, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.077 | 12/47 (MIA PaCa-2, Hs 766T, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1962.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.553×** | -5.9 | 3e-06 | 28/46 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.711×** | -4.9 | 3e-04 | 23/45 (MIA PaCa-2, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.619×** | -4.8 | 3e-04 | 24/46 (MIA PaCa-2, CHP-212, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.441×** | -4.3 | 0.002 | 22/43 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.682×** | -3.9 | 0.013 | 19/45 (A498, HepG2/C3A, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.485×** | -3.8 | 0.013 | 20/43 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.489×** | -3.8 | 0.014 | 20/43 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.712×** | -3.4 | 0.044 | 13/46 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.725×** | -3.2 | 0.074 | 12/46 (NCI-H1573, SW480, …) | two highest doses | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.642×** | -3.2 | 0.082 | 15/46 (Hs 766T, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 23.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -11.0) ⚠ cell-cycle shift, explains ~85% of this change |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 2 | — | [[Pyridoxine (drug)]] 0.5 µM 0.123× (z -10.3) |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 2 | — | [[Saquinavir (drug)]] 0.5 µM 0.118× (z -9.4) |
| [[A498 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -8.7) ⚠ cell-cycle shift, explains ~85% of this change |
| [[HepG2_C3A (line)]] | wt | 9.36 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0383× (z -10.7) ⚠ cell-cycle shift, explains ~84% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -11.7) ⚠ cell-cycle shift, explains ~85% of this change |
| [[NCI-H1573 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.105× (z -9.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0293× (z -20.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 7.32 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0956× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 9.60 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO7]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[GABARAPL1]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[HSD17B7P2]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[BABAM1]] | +0.58 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[CALCOCO2]] | +0.58 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SMPDL3A]] | +0.58 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[WBP2]] | +0.57 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SARAF]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[EFCAB7]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[MKRN1]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[UBFD1]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.55 | +0.61 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFN1]] | -0.60 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[SNRPB]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[POLR1G]] | -0.55 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[MYO19]] | -0.52 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[PBX3]] | -0.51 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SIPA1L3]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[THSD4]] | -0.50 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[CEP83]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ATP13A3]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[SDCCAG8]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[NOP56]] | -0.48 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ACER3]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LURAP1L]] | B | LURAP1L activity raises ABHD4's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 1.46× lower at baseline in the lines without LURAP1L | 0.049 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers ABHD4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PIK3CA]] | B | PIK3CA activity lowers ABHD4's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-0.0, -47.4); signed map (-30.0, -21.7). **Vector** length 108, 25.5% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.7 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.0 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.9 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.7 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -5.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -3.3 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -2.8 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[EX229 (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 4, N-acyl phospholipase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,598,290-22,612,963 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12816 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Hallmark sets | P53_PATHWAY |
| Reactome | 4 pathways, smallest: Acyl chain remodelling of PE; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB40](https://www.uniprot.org/uniprotkb/Q8TB40) ((Lyso)-N-acylphosphatidylethanolamine lipase):

> Lysophospholipase selective for N-acyl phosphatidylethanolamine (NAPE). Contributes to the biosynthesis of N-acyl ethanolamines, including the endocannabinoid anandamide by hydrolyzing the sn-1 and sn-2 acyl chains from N-acyl phosphatidylethanolamine (NAPE) generating glycerophospho-N-acyl ethanolamine (GP-NAE), an intermediate for N-acyl ethanolamine biosynthesis. Hydrolyzes substrates bearing saturated, monounsaturated, polyunsaturated N-acyl chains. Shows no significant activity towards …

**Summary**, from NCBI Gene [63874](https://www.ncbi.nlm.nih.gov/gene/63874):

> Predicted to enable lysophosphatidic acid acyltransferase activity and phosphatidylcholine lysophospholipase A1 activity. Predicted to be involved in N-acylphosphatidylethanolamine metabolic process; lipid homeostasis; and phosphatidic acid biosynthetic process. Predicted to act upstream of or within N-acylethanolamine metabolic process. Predicted to be located in endoplasmic reticulum membrane. Predicted to be active in lipid droplet. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20154) · Entrez [63874](https://www.ncbi.nlm.nih.gov/gene/63874) · UniProt [Q8TB40](https://www.uniprot.org/uniprotkb/Q8TB40) · Ensembl [ENSG00000100439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100439)

## Data

Gene col 1962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1962); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1962]; `tensor/DDL_lfc|DDL_z.npy` [1962]; `embed/gene_vectors.npy` [1962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1962 or target_col == 1962). Every well: [[ABHD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
