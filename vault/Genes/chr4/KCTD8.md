---
symbol: "KCTD8"
type: "gene"
col: 11457
ensembl_id: "ENSG00000183783"
name: "potassium channel tetramerization domain containing 8"
location: "4p13"
module: 9
arm: "+"
pooled_cpm: 8.51
n_lines_expressing: 20
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# KCTD8

*potassium channel tetramerization domain containing 8* — 4p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.62× (z +26.0, q 0e+00, up in 10 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.139×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.161×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.117×); [[Decitabine (drug)]] 0.05 µM in 1 line (CHP-212 0.0757×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRFN2]] (+0.70, fdr 7e-06), [[KHDRBS2]] (+0.68, fdr 7e-06), [[CACNB2]] (+0.68, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[NYAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.62×** | +26.0 | 0e+00 | 10/15 (H4, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +13.2 | 5e-37 | 1/8 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.25×** | +12.2 | 6e-32 | 12/17 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.04×** | +11.8 | 3e-30 | 7/15 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +11.3 | 2e-27 | 6/15 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +10.9 | 2e-25 | 2/12 (HOP62, NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +8.5 | 2e-15 | 10/17 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +7.7 | 1e-12 | 10/14 (H4, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +7.2 | 5e-11 | 7/14 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +7.1 | 8e-11 | 9/16 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +6.2 | 3e-08 | 6/15 (NCI-H2347, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +5.9 | 2e-07 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.7 | 1e-04 | 9/15 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.5 | 3e-04 | 2/12 (NCI-H1792, H4) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +4.4 | 4e-04 | 5/17 (LOX-IMVI, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +4.2 | 8e-04 | 5/15 (NCI-H1573, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.026 | 4/15 (HOP62, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.046 | 3/16 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.085 | 4/17 (SNU-423, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11457.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.139×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.161×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.117×); [[Decitabine (drug)]] 0.05 µM in 1 line (CHP-212 0.0757×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | 0.817× | -3.1 | 0.90 | 3/17 (SHP-77, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 33.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.85× (z +14.9) | — |
| [[SHP-77 (line)]] | alt | 257 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -15.8) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 63.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -12.4) |
| [[BT-474 (line)]] | alt | 6.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.14× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.6× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 2.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.50× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 3.40 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 10.6× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 4.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.57× (z +8.7) | — |
| [[A-172 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRFN2]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[KHDRBS2]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[CACNB2]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[GALNT13]] | +0.66 | +0.58 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SYT4]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[LINC02197]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[KCNB2]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 | same gene group |
| [[LINC02492]] | +0.64 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RIT2]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[CDH10]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ASCL1]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[RUNX1T1]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCTD8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RIT2]] | C | RIT2 activity raises KCTD8's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.73× lower at baseline in the lines without RIT2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[LRATD1]] | C | LRATD1 activity raises KCTD8's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without LRATD1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises KCTD8's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.66× lower at baseline in the lines without KCNB2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises KCTD8's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 5.19× lower at baseline in the lines without NETO1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[MIR646HG]] | C | MIR646HG activity raises KCTD8's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.25× lower at baseline in the lines without MIR646HG | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |
| [[NOVA1]] | C | NOVA1 activity raises KCTD8's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without NOVA1 | 0.095 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[SNTG1]] | C | SNTG1 activity raises KCTD8's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 3.44× lower at baseline in the lines without SNTG1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NYAP2]] | B | KCTD8 activity raises NYAP2's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 2.09× lower at baseline in the lines without KCTD8 | 0.081 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1 |
| [[NOVA1]] | C | KCTD8 activity raises NOVA1's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 5.66× lower at baseline in the lines without KCTD8 | 0.032 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1; co-absent with the target |
| [[SPOCK3]] | C | KCTD8 activity raises SPOCK3's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without KCTD8 | 0.034 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1; co-absent with the target |
| [[ADAMTS3]] | C | KCTD8 activity raises ADAMTS3's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 3.01× lower at baseline in the lines without KCTD8 | 0.035 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1; co-absent with the target |
| [[LRATD1]] | C | KCTD8 activity raises LRATD1's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 1.75× lower at baseline in the lines without KCTD8 | 0.076 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1; co-absent with the target |
| [[GUCY1A1]] | C | KCTD8 activity raises GUCY1A1's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 2.20× lower at baseline in the lines without KCTD8 | 0.091 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.0, 36.9); signed map (43.6, 34.7). **Vector** length 43.0, 10.9% of its response variance represented; |z| ≥ 3 in 410 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.50 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +26.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +8.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.6 | -0.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p13 — chr4:44,173,903-44,448,809 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZWB6](https://www.uniprot.org/uniprotkb/Q6ZWB6) (BTB/POZ domain-containing protein KCTD8):

> Auxiliary subunit of GABA-B receptors that determine the pharmacology and kinetics of the receptor response. Increases agonist potency and markedly alter the G protein signaling of the receptors by accelerating onset and promoting desensitization (By similarity).

**Summary**, from NCBI Gene [386617](https://www.ncbi.nlm.nih.gov/gene/386617):

> Predicted to enable obsolete G protein-coupled neurotransmitter receptor activity involved in regulation of presynaptic membrane potential. Predicted to be involved in regulation of G protein-coupled receptor signaling pathway. Predicted to be located in postsynaptic membrane. Predicted to be part of signaling receptor complex. Predicted to be active in postsynapse and presynaptic active zone membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22394) · Entrez [386617](https://www.ncbi.nlm.nih.gov/gene/386617) · UniProt [Q6ZWB6](https://www.uniprot.org/uniprotkb/Q6ZWB6) · Ensembl [ENSG00000183783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183783)

## Data

Gene col 11457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11457); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11457]; `tensor/DDL_lfc|DDL_z.npy` [11457]; `embed/gene_vectors.npy` [11457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11457 or target_col == 11457). Every well: [[KCTD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
