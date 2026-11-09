---
symbol: "CACNA2D2"
type: "gene"
col: 147
ensembl_id: "ENSG00000007402"
name: "calcium voltage-gated channel auxiliary subunit alpha2delta 2"
location: "3p21.31"
module: 102
arm: "+"
pooled_cpm: 2.21
n_lines_expressing: 33
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 20
direction_downstream: 3
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# CACNA2D2

*calcium voltage-gated channel auxiliary subunit alpha2delta 2* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.87× (z +13.1, q 1e-36, up in 13 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.121×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SW1417 0.0607×; ⚠ toxic; cell-cycle shift, explains ~44% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (AN3 CA 0.0615×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH23]] (+0.68, fdr 7e-06), [[KCNQ2]] (+0.68, fdr 7e-06), [[LINC00937]] (+0.65, fdr 1e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[NFASC]] → it (grade B ⚠); 3 go from it, the strongest it → [[SYN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.87×** | +13.1 | 1e-36 | 13/21 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.39×** | +12.5 | 1e-33 | 1/1 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +12.4 | 3e-33 | 11/20 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.84×** | +11.9 | 2e-30 | 19/28 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.49×** | +11.4 | 7e-28 | 18/26 (SW1417, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.31×** | +10.6 | 4e-24 | 18/27 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +9.7 | 3e-20 | 2/8 (SW480, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.68×** | +8.7 | 3e-16 | 18/28 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.66×** | +8.0 | 9e-14 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **2.02×** | +5.9 | 2e-07 | 2/9 (A-427, SW1417) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +5.8 | 3e-07 | 6/27 (SW480, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +5.4 | 4e-06 | 6/22 (SW 900, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +5.2 | 8e-06 | 10/21 (A-427, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.25×** | +5.1 | 1e-05 | 1/5 (NCI-H2030) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.74×** | +4.9 | 4e-05 | 14/28 (SW1417, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.7 | 8e-05 | 7/28 (J82, A-172, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +4.0 | 0.002 | 4/18 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.63×** | +3.9 | 0.002 | 3/13 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.50×** | +3.5 | 0.010 | 2/15 (A-172, SW 900) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.023 | 5/19 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.035 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 147.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.121×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SW1417 0.0607×; ⚠ toxic; cell-cycle shift, explains ~44% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (AN3 CA 0.0615×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Malotilate (drug)]] 5 µM |  | 0.704× | -3.1 | 0.59 | 2/27 (SW 900, PANC-1) | rises with dose | position effect removed |
| [[Erythromycin (drug)]] 0.05 µM |  | 0.708× | -3.1 | 0.59 | 3/27 (NCI-H1573, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.01 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 7.91 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.21× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0607× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.7) |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0615× (z -9.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 2.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +8.6) | — |
| [[A-172 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.645 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.846 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.711 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.684 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.772 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.802 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.867 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.789 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.519 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH23]] | +0.68 | +0.69 / +0.70 | both halves | 7e-06 | pathway: Sensory Perception |
| [[KCNQ2]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 | pathway: Neuronal System |
| [[LINC00937]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[LRRC4B]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 | pathway: Neuronal System |
| [[RHBDL3]] | +0.64 | +0.60 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LMX1B]] | +0.62 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[SDK2]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MYT1]] | +0.61 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[TCF7L1]] | +0.61 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[SEPTIN3]] | +0.60 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[RET]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[RASSF2]] | +0.59 | +0.40 / +0.60 | both halves | 5e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 11, C 9. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFASC]] | B | NFASC activity raises CACNA2D2's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.17× lower at baseline in the lines without NFASC | 0.004 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[KCNQ2]] | B | KCNQ2 activity raises CACNA2D2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.67× lower at baseline in the lines without KCNQ2 | 0.006 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[RAB39A]] | B | RAB39A activity raises CACNA2D2's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.98× lower at baseline in the lines without RAB39A | 0.022 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[DPYSL5]] | B | DPYSL5 activity raises CACNA2D2's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without DPYSL5 | 0.031 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[TOP2A]] | B | TOP2A activity lowers CACNA2D2's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KREMEN2]] | B | KREMEN2 activity raises CACNA2D2's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without KREMEN2 | 0.051 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[SDK2]] | B | SDK2 activity raises CACNA2D2's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without SDK2 | 0.061 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent |
| [[SLC16A10]] | B | SLC16A10 activity raises CACNA2D2's level | lines that do not express SLC16A10 (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without SLC16A10 | 0.069 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2 |
| [[SEMA6B]] | B | SEMA6B activity raises CACNA2D2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.68× lower at baseline in the lines without SEMA6B | 0.088 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[GNAO1]] | B | GNAO1 activity raises CACNA2D2's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 1.51× lower at baseline in the lines without GNAO1 | 0.089 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[GBX1]] | B | GBX1 activity raises CACNA2D2's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.67× lower at baseline in the lines without GBX1 | 0.099 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[JPH3]] | C | JPH3 activity raises CACNA2D2's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 2.27× lower at baseline in the lines without JPH3 | 0.017 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYN2]] | B | CACNA2D2 activity raises SYN2's level | lines that do not express CACNA2D2 (17) vs lines expressing it (33) | 2.21× lower at baseline in the lines without CACNA2D2 | 0.094 | ⚠ within organs, on part of the lines; also absent: JPH3, MIR9-3HG, CELF4; maybe low, not absent |
| [[STOX2]] | C | CACNA2D2 activity raises STOX2's level | lines that do not express CACNA2D2 (17) vs lines expressing it (33) | 2.91× lower at baseline in the lines without CACNA2D2 | 0.089 | ⚠ within organs, on part of the lines; also absent: JPH3, MIR9-3HG, CELF4; maybe low, not absent; co-absent with the target |
| [[LMX1B]] | C | CACNA2D2 activity raises LMX1B's level | lines that do not express CACNA2D2 (17) vs lines expressing it (33) | 3.19× lower at baseline in the lines without CACNA2D2 | 0.090 | ⚠ within organs, on part of the lines; also absent: JPH3, MIR9-3HG, CELF4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.9, 38.0); signed map (26.8, 26.2). **Vector** length 37.9, 5.47% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | -0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -0.4 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit alpha2delta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,362,613-50,504,244 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0558, alpha2delta-2 |
| Gene groups (HGNC) | Calcium voltage-gated channel auxiliary alpha2delta subunits |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 13 pathways, smallest: Phase 2 - plateau phase; Presynaptic depolarization and calcium channel opening; Adrenaline,noradrenaline inhibits insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY47](https://www.uniprot.org/uniprotkb/Q9NY47) (Voltage-dependent calcium channel subunit alpha-2/delta-2):

> The alpha-2/delta subunit of voltage-dependent calcium channels regulates calcium current density and activation/inactivation kinetics of the calcium channel. Acts as a regulatory subunit for P/Q-type calcium channel (CACNA1A), N-type (CACNA1B), L-type (CACNA1C OR CACNA1D) and possibly T-type (CACNA1G). Overexpression induces apoptosis.

**Summary**, from NCBI Gene [9254](https://www.ncbi.nlm.nih.gov/gene/9254):

> Calcium channels mediate the entry of calcium ions into the cell upon membrane polarization. This gene encodes the alpha-2/delta subunit of the voltage-dependent calcium channel complex. The complex consists of the main channel-forming subunit alpha-1, and auxiliary subunits alpha-2/delta, beta, and gamma. The auxiliary subunits function in the assembly and membrane localization of the complex, and modulate calcium currents and channel activation/inactivation kinetics. The subunit encoded by …

**Accessions** — [HGNC:1400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1400) · Entrez [9254](https://www.ncbi.nlm.nih.gov/gene/9254) · UniProt [Q9NY47](https://www.uniprot.org/uniprotkb/Q9NY47) · Ensembl [ENSG00000007402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007402)

## Data

Gene col 147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 147); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 147]; `tensor/DDL_lfc|DDL_z.npy` [147]; `embed/gene_vectors.npy` [147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 147 or target_col == 147). Every well: [[CACNA2D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNA2D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
