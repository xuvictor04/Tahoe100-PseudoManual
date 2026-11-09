---
symbol: "ENPP2"
type: "gene"
col: 5951
ensembl_id: "ENSG00000136960"
name: "ectonucleotide pyrophosphatase/phosphodiesterase 2"
location: "8q24.12"
module: 9
arm: "+"
pooled_cpm: 4.41
n_lines_expressing: 24
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 15
direction_downstream: 15
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ENPP2

*ectonucleotide pyrophosphatase/phosphodiesterase 2* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 10.3× (z +20.4, q 0e+00, up in 18 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.0897×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0547×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CHP-212 0.148×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGP]] (+0.65, fdr 1e-05), [[LDB2]] (+0.57, fdr 1e-05), [[ARHGAP28]] (+0.57, fdr 1e-05); moves opposite to [[DNAAF10]] (-0.43, fdr 7e-04), [[LINC01145-1]] (-0.41, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 15 go from it, the strongest it → [[GRIK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5951.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **10.3×** | +20.4 | 0e+00 | 18/20 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.97×** | +17.1 | 0e+00 | 12/18 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.72×** | +16.7 | 0e+00 | 19/19 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.31×** | +14.8 | 0e+00 | 20/20 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +14.7 | 0e+00 | 7/17 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.04×** | +14.2 | 1e-43 | 15/19 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.31×** | +14.1 | 4e-43 | 1/4 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.82×** | +13.8 | 2e-41 | 6/12 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.38×** | +9.9 | 3e-21 | 1/5 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.79×** | +9.0 | 2e-17 | 15/19 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.66×** | +8.6 | 5e-16 | 17/20 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +6.1 | 4e-08 | 5/19 (SW480, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +5.9 | 1e-07 | 5/18 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.54×** | +5.8 | 3e-07 | 10/18 (SK-MEL-2, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +5.7 | 4e-07 | 4/12 (C32, SW 900, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +4.5 | 2e-04 | 4/19 (RPMI-7951, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.5 | 2e-04 | 2/20 (LOX-IMVI, NCI-H1792) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +4.5 | 3e-04 | 2/20 (C32, SW480) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.2 | 9e-04 | 0/17 | top dose only | cell-cycle shift (explains ~21% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5951.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.0897×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0547×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CHP-212 0.148×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | 0.696× | -3.2 | 0.55 | 3/20 (SW48, SW1417, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.710× | -3.0 | 0.55 | 0/19 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 140 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0897× (z -12.3) |
| [[SW480 (line)]] | alt | 1.34 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 19.9× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 20.0× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 1.72 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 36.9× (z +9.9) | — |
| [[C32 (line)]] | wt | 113 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.89× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 17.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.84× (z +9.3) | — |
| [[A498 (line)]] | wt | 1.29 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 34.9× (z +9.2) | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0487× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 2.67 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 16.5× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 1.76 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 28.5× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0878× (z -9.6) |
| [[A-172 (line)]] | wt | 0.845 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.000 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.773 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.818 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.956 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGP]] | +0.65 | +0.54 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[LDB2]] | +0.57 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ARHGAP28]] | +0.57 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SYT11]] | +0.54 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[ADGRA2]] | +0.52 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[SEMA6A]] | +0.52 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[CCDC144A]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[AMPH]] | +0.52 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ST6GALNAC3]] | +0.51 | +0.26 / +0.56 | both halves | 4e-04 |  |
| [[LINC01194]] | +0.50 | +0.48 / +0.43 | both halves | 4e-05 |  |
| [[ANGPT1]] | +0.50 | +0.44 / +0.63 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[LINC00540]] | +0.50 | +0.41 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF10]] | -0.43 | -0.20 / -0.30 | both halves | 7e-04 |  |
| [[LINC01145-1]] | -0.41 | -0.33 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 4, C 11. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ENPP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GRIK2]] | B | GRIK2 activity raises ENPP2's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without GRIK2 | 0.057 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B |
| [[ATOH8]] | B | ATOH8 activity raises ENPP2's level | lines that do not express ATOH8 (23) vs lines expressing it (27) | 2.51× lower at baseline in the lines without ATOH8 | 0.064 | ⚠ within organs, on part of the lines; also absent: DZIP1, LINC00839, KCNQ5; maybe low, not absent |
| [[TMEM108]] | B | TMEM108 activity raises ENPP2's level | lines that do not express TMEM108 (23) vs lines expressing it (27) | 2.51× lower at baseline in the lines without TMEM108 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: TWIST1, FYB1, GATA3; maybe low, not absent |
| [[PDZRN3]] | C | PDZRN3 activity raises ENPP2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 3.30× lower at baseline in the lines without PDZRN3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098; co-absent with the target |
| [[DCT]] | C | DCT activity raises ENPP2's level | lines that do not express DCT (42) vs lines expressing it (8) | 5.52× lower at baseline in the lines without DCT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[AMPH]] | C | AMPH activity raises ENPP2's level | lines that do not express AMPH (36) vs lines expressing it (14) | 3.52× lower at baseline in the lines without AMPH | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ANKRD30B, GRIN2A, GYPC; co-absent with the target |
| [[DAAM2]] | C | DAAM2 activity raises ENPP2's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 3.04× lower at baseline in the lines without DAAM2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[SCG3]] | C | SCG3 activity raises ENPP2's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 2.11× lower at baseline in the lines without SCG3 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[PPP2R2B]] | C | PPP2R2B activity raises ENPP2's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 2.75× lower at baseline in the lines without PPP2R2B | 0.028 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[P2RX7]] | C | P2RX7 activity raises ENPP2's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.39× lower at baseline in the lines without P2RX7 | 0.039 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent; co-absent with the target |
| [[HMCN1]] | C | HMCN1 activity raises ENPP2's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 3.02× lower at baseline in the lines without HMCN1 | 0.048 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 5, C 10. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIK2]] | B | ENPP2 activity raises GRIK2's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 3.37× lower at baseline in the lines without ENPP2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent |
| [[FKBP7]] | B | ENPP2 activity raises FKBP7's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without ENPP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent |
| [[GLIS1]] | B | ENPP2 activity raises GLIS1's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.79× lower at baseline in the lines without ENPP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent |
| [[CRISPLD2]] | B | ENPP2 activity raises CRISPLD2's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 1.79× lower at baseline in the lines without ENPP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent |
| cells under [[Pralsetinib (drug)]] 5 µM | B | ENPP2 activity raises the cells' numbers under Pralsetinib 5 µM (protects the cells) | lines that do not express ENPP2 (26) vs lines expressing it (22) | the lines without ENPP2: 0.71× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent |
| [[P2RX7]] | C | ENPP2 activity raises P2RX7's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without ENPP2 | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[KCNJ6]] | C | ENPP2 activity raises KCNJ6's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.61× lower at baseline in the lines without ENPP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[PCBP3]] | C | ENPP2 activity raises PCBP3's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 3.70× lower at baseline in the lines without ENPP2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[DAAM2]] | C | ENPP2 activity raises DAAM2's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.09× lower at baseline in the lines without ENPP2 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[SCG3]] | C | ENPP2 activity raises SCG3's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.03× lower at baseline in the lines without ENPP2 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[TMTC1]] | C | ENPP2 activity raises TMTC1's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.90× lower at baseline in the lines without ENPP2 | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[RORB]] | C | ENPP2 activity raises RORB's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without ENPP2 | 0.042 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.394). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.0, 29.9); signed map (35.8, 34.8). **Vector** length 46.0, 9.68% of its response variance represented; |z| ≥ 3 in 569 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +14.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +17.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +6.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.1 | +1.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -2.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleotide pyrophosphatase/phosphodiesterase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:119,557,086-119,673,453 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATX, PD-IALPHA; previously PDNP2 |
| Gene groups (HGNC) | Ectonucleotide pyrophosphatase/phosphodiesterase family |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 6 pathways, smallest: HuR (ELAVL1) binds and stabilizes mRNA; Vitamin B5 (pantothenate) metabolism; Regulation of mRNA stability by proteins that bind AU-rich elements |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13822](https://www.uniprot.org/uniprotkb/Q13822) (Autotaxin):

> Secreted lysophospholipase D that hydrolyzes lysophospholipids to produce the signaling molecule lysophosphatidic acid (LPA) in extracellular fluids. Its major substrate is lysophosphatidylcholine. Can also act on sphingosylphosphorylcholine producing sphingosine-1-phosphate, a modulator of cell motility. Can hydrolyze, in vitro, bis-pNPP, to some extent pNP-TMP, and barely ATP. Involved in several motility-related processes such as angiogenesis and neurite outgrowth. Acts as an angiogenic …

**Summary**, from NCBI Gene [5168](https://www.ncbi.nlm.nih.gov/gene/5168):

> The protein encoded by this gene functions as both a phosphodiesterase, which cleaves phosphodiester bonds at the 5' end of oligonucleotides, and a phospholipase, which catalyzes production of lysophosphatidic acid (LPA) in extracellular fluids. LPA evokes growth factor-like responses including stimulation of cell proliferation and chemotaxis. This gene product stimulates the motility of tumor cells and has angiogenic properties, and its expression is upregulated in several kinds of carcinomas. …

**Accessions** — [HGNC:3357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3357) · Entrez [5168](https://www.ncbi.nlm.nih.gov/gene/5168) · UniProt [Q13822](https://www.uniprot.org/uniprotkb/Q13822) · Ensembl [ENSG00000136960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136960)

## Data

Gene col 5951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5951); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5951]; `tensor/DDL_lfc|DDL_z.npy` [5951]; `embed/gene_vectors.npy` [5951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5951 or target_col == 5951). Every well: [[ENPP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENPP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
