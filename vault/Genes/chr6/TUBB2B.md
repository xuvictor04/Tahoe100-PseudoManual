---
symbol: "TUBB2B"
type: "gene"
col: 5997
ensembl_id: "ENSG00000137285"
name: "tubulin beta 2B class IIb"
location: "6p25.2"
module: 123
arm: "+"
pooled_cpm: 8.62
n_lines_expressing: 33
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# TUBB2B

*tubulin beta 2B class IIb* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.77× (z +13.4, q 3e-38, up in 22 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0600×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0835×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (SNU-423 0.0643×); [[Clobetasol propionate (drug)]] 5 µM in 1 line (NCI-H1573 0.0261×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUND]] (+0.69, fdr 1e-05), [[NDRG4]] (+0.67, fdr 7e-06), [[SLC41A2]] (+0.66, fdr 9e-06); moves opposite to [[TOR1A]] (-0.59, fdr 3e-05), [[PHC2-AS1]] (-0.57, fdr 4e-05), [[HCFC1]] (-0.57, fdr 1e-04).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[P2RX7]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ARHGEF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.77×** | +13.4 | 3e-38 | 22/26 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.52×** | +9.0 | 8e-17 | 24/30 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.45×** | +8.5 | 3e-15 | 21/29 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.06×** | +7.3 | 4e-11 | 21/30 (J82, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.62×** | +6.9 | 7e-10 | 23/30 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.43×** | +6.3 | 2e-08 | 17/22 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.32×** | +6.0 | 2e-07 | 21/30 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.26×** | +5.8 | 4e-07 | 20/30 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +5.5 | 3e-06 | 19/27 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.04×** | +5.1 | 2e-05 | 8/20 (HepG2/C3A, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +4.6 | 2e-04 | 17/29 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.86×** | +4.4 | 4e-04 | 18/29 (SHP-77, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.82×** | +4.1 | 0.002 | 3/13 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +4.1 | 0.002 | 16/30 (J82, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.9 | 0.004 | 5/21 (HepG2/C3A, NCI-H661, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +3.8 | 0.005 | 14/27 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[venetoclax (drug)]] 5 µM |  | **2.40×** | +3.3 | 0.036 | 9/23 (HOP62, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +3.1 | 0.052 | 11/29 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.059 | 7/30 (HOP62, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5997.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0600×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0835×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (SNU-423 0.0643×); [[Clobetasol propionate (drug)]] 5 µM in 1 line (NCI-H1573 0.0261×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.639× | -3.2 | 0.32 | 6/30 (HS-578T, HOP62, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.642× | -3.2 | 0.32 | 11/30 (NCI-H1573, NCI-H2347, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.431× | -3.1 | 0.32 | 13/28 (AN3 CA, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 5.79 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +11.8) | [[TAK-901 (drug)]] 0.05 µM 0.0600× (z -11.0) |
| [[PANC-1 (line)]] | alt | 13.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +19.2) | — |
| [[NCI-H1573 (line)]] | alt | 2.48 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 35.9× (z +12.6) | [[Clobetasol propionate (drug)]] 5 µM 0.0261× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 43.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.33× (z +14.7) | — |
| [[HOP62 (line)]] | alt | 26.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +14.2) | — |
| [[AN3 CA (line)]] | alt | 60.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0835× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 6.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 2.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 3.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 5.38 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0628× (z -8.6) |
| [[SNU-423 (line)]] | alt | 9.77 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0643× (z -9.7) |
| [[A-172 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.898 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUND]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[NDRG4]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SLC41A2]] | +0.66 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[PIM3]] | +0.65 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[TUBB2A]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 | same gene group; pathway: Activation of AMPK downstream of NMDARs; STRING 933 |
| [[CYRIA]] | +0.65 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[NEURL3]] | +0.63 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[KLF2]] | +0.63 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ATF4]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[RPLP0P2]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[DUSP8]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[TNFRSF9]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOR1A]] | -0.59 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[PHC2-AS1]] | -0.57 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[HCFC1]] | -0.57 | -0.35 / -0.62 | both halves | 1e-04 | pathway: Organelle biogenesis and maintenance |
| [[MSL3]] | -0.57 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[PSME3]] | -0.55 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[METTL9]] | -0.55 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.55 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[XNDC1N]] | -0.55 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[DARS2]] | -0.55 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[DPAGT1]] | -0.55 | -0.42 / -0.57 | both halves | 4e-05 | pathway: Asparagine N-linked glycosylation |
| [[NUP155]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[ERLIN2]] | -0.55 | -0.16 / -0.62 | ⚠ one half (not replicated) | 0.001 |  |
| [[LAMB1]] | -0.54 | -0.44 / -0.52 | both halves | 3e-05 | pathway: L1CAM interactions |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RX7]] | B | P2RX7 activity raises TUBB2B's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without P2RX7 | 0.065 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[SYT11]] | B | SYT11 activity raises TUBB2B's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without SYT11 | 0.084 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[HES4]] | C | HES4 activity lowers TUBB2B's level | lines that do not express HES4 (4) vs lines expressing it (46) | 4.61× higher at baseline in the lines without HES4 | 0.052 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF3]] | B | TUBB2B activity raises ARHGEF3's level | lines that do not express TUBB2B (17) vs lines expressing it (33) | 1.30× lower at baseline in the lines without TUBB2B | 0.097 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, MAP6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.1, -0.1); signed map (-0.2, 22.0). **Vector** length 62.7, 14.5% of its response variance represented; |z| ≥ 3 in 579 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +1.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -1.9 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | tubulin beta 2B class IIb |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:3,223,324-3,231,730 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC8685, DKFZp566F223, bA506K6.1 |
| Gene groups (HGNC) | Tubulin beta family |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 83 pathways, smallest: Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane; Transport of connexons to the plasma membrane; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVA1](https://www.uniprot.org/uniprotkb/Q9BVA1) (Tubulin beta-2B chain):

> Tubulin is the major constituent of microtubules, a cylinder consisting of laterally associated linear protofilaments composed of alpha- and beta-tubulin heterodimers. Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms. Below the cap, tubulin dimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin. Plays a critical role in proper axon guidance in both central and peripheral axon tracts. Implicated in neuronal migration.

**Summary**, from NCBI Gene [347733](https://www.ncbi.nlm.nih.gov/gene/347733):

> The protein encoded by this gene is a beta isoform of tubulin, which binds GTP and is a major component of microtubules. This gene is highly similar to TUBB2A and TUBB2C. Defects in this gene are a cause of asymmetric polymicrogyria. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:30829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30829) · Entrez [347733](https://www.ncbi.nlm.nih.gov/gene/347733) · UniProt [Q9BVA1](https://www.uniprot.org/uniprotkb/Q9BVA1) · Ensembl [ENSG00000137285](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137285)

## Data

Gene col 5997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5997); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5997]; `tensor/DDL_lfc|DDL_z.npy` [5997]; `embed/gene_vectors.npy` [5997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5997 or target_col == 5997). Every well: [[TUBB2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBB2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
