---
symbol: "RAB32"
type: "gene"
col: 3997
ensembl_id: "ENSG00000118508"
name: "RAB32, member RAS oncogene family"
location: "6q24.3"
module: 14
arm: "+"
pooled_cpm: 8.92
n_lines_expressing: 43
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 11
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RAB32

*RAB32, member RAS oncogene family* — 6q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +7.5, q 3e-11, up in 23 of 38 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.10× (z +6.9, q 2e-09, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.326× (z -10.5, q 6e-23, down in 35 of 40 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (HepG2/C3A 0.0706×, Hs 766T 0.145×, J82 0.182×, Panc 03.27 0.121×; ⚠ cell-cycle shift, explains ~32% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (HepG2/C3A 0.0894×, A-172 0.176×, Hs 766T 0.160×, J82 0.199×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.0818×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRAM1]] (+0.67, fdr 7e-06), [[PLEKHM2]] (+0.65, fdr 7e-06), [[RRAGC]] (+0.64, fdr 7e-06); moves opposite to [[BCAP31]] (-0.59, fdr 1e-05), [[COL13A1]] (-0.56, fdr 1e-05), [[HPCAL1]] (-0.55, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 11 go from it, the strongest it → [[ITGB5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.77×** | +7.5 | 3e-11 | 23/38 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.10×** | +6.9 | 2e-09 | 24/40 (MIA PaCa-2, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.84×** | +5.5 | 8e-06 | 21/38 (J82, A-172, …) | rises with dose | composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.46×** | +5.0 | 7e-05 | 24/40 (NCI-H23, NCI-H1573, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.65×** | +4.7 | 3e-04 | 18/36 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.7 | 3e-04 | 15/32 (NCI-H2030, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.60×** | +4.4 | 8e-04 | 17/37 (NCI-H23, SNU-423, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.57×** | +4.2 | 0.002 | 23/40 (BT-474, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +4.1 | 0.002 | 13/23 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.003 | 13/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.004 | 18/40 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.005 | 16/41 (NCI-H460, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.77×** | +3.7 | 0.008 | 15/37 (LOX-IMVI, HS-578T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.008 | 17/40 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.008 | 14/40 (SK-MEL-2, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.024 | 15/41 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.024 | 12/40 (hTERT-HPNE, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.038 | 15/41 (SK-MEL-2, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +3.2 | 0.040 | 13/37 (A-172, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.063 | 12/41 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.067 | 6/40 (NCI-H1573, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3997.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (HepG2/C3A 0.0706×, Hs 766T 0.145×, J82 0.182×, Panc 03.27 0.121×; ⚠ cell-cycle shift, explains ~32% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (HepG2/C3A 0.0894×, A-172 0.176×, Hs 766T 0.160×, J82 0.199×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.0818×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.326×** | -10.5 | 6e-23 | 35/40 (HepG2/C3A, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.367×** | -9.4 | 2e-18 | 35/40 (HepG2/C3A, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.459×** | -7.3 | 7e-11 | 27/40 (BT-474, AsPC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.601×** | -4.6 | 7e-04 | 19/37 (HS-578T, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.67 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +12.5) ⚠ cell-cycle shift, explains ~44% of this change | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -9.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 15.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +10.8) ⚠ cell-cycle shift, explains ~44% of this change | [[Panobinostat (drug)]] 5 µM 0.182× (z -9.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0706× (z -11.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -9.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 9.80 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.104× (z -8.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H2347 (line)]] | alt | 5.80 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0818× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 8.02 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.695 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAM1]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PLEKHM2]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.64 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[RAB9A]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 | same gene group; pathway: RAB GEFs exchange GTP for GDP on RABs |
| [[SLC2A6]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ZBTB10]] | +0.62 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[DUSP16]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FILIP1L]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[HPS1]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 | pathway: RAB GEFs exchange GTP for GDP on RABs; STRING 693 |
| [[NEURL3]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CPEB2]] | +0.58 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[PIGP]] | +0.57 | +0.41 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[COL13A1]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[HPCAL1]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[RRM2]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ODF2]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[WWTR1]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[MYCBP]] | -0.53 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[CHID1]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RNGTT]] | -0.53 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ETV5]] | -0.52 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ARHGAP4]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PMPCA]] | -0.51 | -0.59 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RAB32's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DENND5A]] | C | DENND5A activity raises RAB32's level | lines that do not express DENND5A (3) vs lines expressing it (47) | 3.75× lower at baseline in the lines without DENND5A | 0.069 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB5]] | B | RAB32 activity raises ITGB5's level | lines that do not express RAB32 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without RAB32 | 0.027 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[SWAP70]] | B | RAB32 activity raises SWAP70's level | lines that do not express RAB32 (7) vs lines expressing it (43) | 1.53× lower at baseline in the lines without RAB32 | 0.046 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[PDGFC]] | B | RAB32 activity raises PDGFC's level | lines that do not express RAB32 (7) vs lines expressing it (43) | 5.59× lower at baseline in the lines without RAB32 | 0.050 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[KIF13A]] | B | RAB32 activity raises KIF13A's level | lines that do not express RAB32 (7) vs lines expressing it (43) | 1.76× lower at baseline in the lines without RAB32 | 0.058 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[ODF2]] | B | RAB32 activity lowers ODF2's level | lines that do not express RAB32 (7) vs lines expressing it (43) | 1.16× higher at baseline in the lines without RAB32 | 0.069 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| cells under [[olaparib (drug)]] 5 µM | B | RAB32 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express RAB32 (7) vs lines expressing it (41) | the lines without RAB32: 1.45× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | B | RAB32 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express RAB32 (7) vs lines expressing it (41) | the lines without RAB32: 0.82× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| cells under [[PH-797804 (drug)]] 0.05 µM | B | RAB32 activity lowers the cells' numbers under PH-797804 0.05 µM (makes them more sensitive) | lines that do not express RAB32 (7) vs lines expressing it (41) | the lines without RAB32: 1.26× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | B | RAB32 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express RAB32 (7) vs lines expressing it (41) | the lines without RAB32: 0.78× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | B | RAB32 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express RAB32 (7) vs lines expressing it (41) | the lines without RAB32: 0.57× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | B | RAB32 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express RAB32 (7) vs lines expressing it (41) | the lines without RAB32: 1.33× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, 9.5); signed map (-6.9, 0.1). **Vector** length 88.4, 22.4% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +6.7 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.1 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.8 | +3.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.2 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.9 | +3.0 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.3 | -10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.0 | -9.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.2 | -7.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Quinestrol (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RAB32, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.3 — chr6:146,543,833-146,554,953 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases; A-kinase anchoring proteins |
| Reactome | 5 pathways, smallest: RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13637](https://www.uniprot.org/uniprotkb/Q13637) (Ras-related protein Rab-32):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. Also acts as an A-kinase anchoring protein by binding to the type II regulatory subunit of protein kinase A and …

**Summary**, from NCBI Gene [10981](https://www.ncbi.nlm.nih.gov/gene/10981):

> The protein encoded by this gene anchors the type II regulatory subunit of protein kinase A to the mitochondrion and aids in mitochondrial fission. The encoded protein also appears to be involved in autophagy and melanosome secretion. Variations in this gene may be linked to leprosy. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:9772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9772) · Entrez [10981](https://www.ncbi.nlm.nih.gov/gene/10981) · UniProt [Q13637](https://www.uniprot.org/uniprotkb/Q13637) · Ensembl [ENSG00000118508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118508)

## Data

Gene col 3997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3997); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3997]; `tensor/DDL_lfc|DDL_z.npy` [3997]; `embed/gene_vectors.npy` [3997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3997 or target_col == 3997). Every well: [[RAB32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
