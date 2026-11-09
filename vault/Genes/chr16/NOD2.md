---
symbol: "NOD2"
type: "gene"
col: 9436
ensembl_id: "ENSG00000167207"
name: "nucleotide binding oligomerization domain containing 2"
location: "16q12.1"
module: 14
arm: "+"
pooled_cpm: 2.94
n_lines_expressing: 33
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 13
direction_downstream: 26
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NOD2

*nucleotide binding oligomerization domain containing 2* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.84× (z +7.3, q 2e-10, up in 15 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.426× (z -7.2, q 2e-10, down in 20 of 29 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 0.629× (z -3.9, q 0.014, down in 8 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPAMD8]] (+0.61, fdr 1e-05), [[TNFAIP2]] (+0.57, fdr 3e-05), [[TNFAIP6]] (+0.56, fdr 4e-05); moves opposite to [[VKORC1L1]] (-0.45, fdr 1e-04), [[GBX2-AS1]] (-0.45, fdr 3e-05), [[PBX3]] (-0.43, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LINC01285]] → it (grade B ⚠); 26 go from it, the strongest it → [[NCALD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +7.3 | 2e-10 | 15/30 (Panc 03.27, COLO 205, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +5.8 | 2e-06 | 9/27 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +4.7 | 5e-04 | 7/25 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.044 | 7/23 (MIA PaCa-2, LoVo, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.47× | +3.3 | 0.11 | 3/30 (Hs 766T, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.44× | +3.2 | 0.11 | 5/30 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 2.06× | +3.2 | 0.12 | 11/28 (LoVo, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.03× | +3.1 | 0.13 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.43× | +3.0 | 0.17 | 2/13 (LoVo, BT-474) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.426×** | -7.2 | 2e-10 | 20/29 (HS-578T, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.427×** | -7.2 | 2e-10 | 19/29 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.483×** | -6.1 | 2e-07 | 20/31 (RPMI-7951, NCI-H1573, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.629×** | -3.9 | 0.014 | 8/30 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.634×** | -3.8 | 0.014 | 13/30 (SNU-423, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.644×** | -3.6 | 0.033 | 10/22 (LS 180, RPMI-7951, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.745×** | -3.5 | 0.033 | 13/30 (HepG2/C3A, SW 1088, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.745×** | -3.5 | 0.033 | 12/30 (A549, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.674×** | -3.3 | 0.051 | 12/30 (HCT15, RPMI-7951, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.579×** | -3.3 | 0.051 | 8/23 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | **0.677×** | -3.3 | 0.051 | 7/30 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.677×** | -3.3 | 0.051 | 5/30 (Hs 766T, A549, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.696× | -3.0 | 0.10 | 9/30 (SHP-77, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.59 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0333× (z -15.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.7) |
| [[Hs 766T (line)]] | wt | 7.97 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0916× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Elagolix sodium (drug)]] 0.5 µM 0.0945× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0308× (z -16.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[CFPAC-1 (line)]] | alt | 5.42 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0524× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 4.36 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0284× (z -11.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 5.12 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0842× (z -10.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.644 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPAMD8]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.57 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[TNFAIP6]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[SOD2]] | +0.55 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[IRF1]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 443 |
| [[MAP3K8]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 | pathway: Interleukin-1 family signaling |
| [[TMPRSS3]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[GCA]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ANO9]] | +0.53 | +0.54 / +0.46 | both halves | 3e-05 | pathway: SARS-CoV-2 Infection |
| [[EFNA1]] | +0.53 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[BCL3]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CCL5]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 515 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1L1]] | -0.45 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[GBX2-AS1]] | -0.45 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PBX3]] | -0.43 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[MIR100HG]] | -0.43 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[ENG]] | -0.43 | -0.38 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 8, C 5. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01285]] | B | LINC01285 activity raises NOD2's level | lines that do not express LINC01285 (21) vs lines expressing it (29) | 2.19× lower at baseline in the lines without LINC01285 | 0.010 | ⚠ within organs, on part of the lines; also absent: HNF1A, SLC22A3, LINC01819; maybe low, not absent |
| [[TMPRSS3]] | B | TMPRSS3 activity raises NOD2's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without TMPRSS3 | 0.017 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[COL16A1]] | B | COL16A1 activity raises NOD2's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.00× lower at baseline in the lines without COL16A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[TRIM29]] | B | TRIM29 activity raises NOD2's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without TRIM29 | 0.019 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[LINC02405]] | B | LINC02405 activity raises NOD2's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without LINC02405 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360 |
| [[NCALD]] | B | NCALD activity raises NOD2's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.64× lower at baseline in the lines without NCALD | 0.059 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[RASSF5]] | B | RASSF5 activity raises NOD2's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 2.54× lower at baseline in the lines without RASSF5 | 0.072 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[CGNL1]] | B | CGNL1 activity raises NOD2's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without CGNL1 | 0.073 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[ELF3-AS1]] | C | ELF3-AS1 activity raises NOD2's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.01× lower at baseline in the lines without ELF3-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent; co-absent with the target |
| [[STAT5A]] | C | STAT5A activity raises NOD2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 2.56× lower at baseline in the lines without STAT5A | 0.045 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2; co-absent with the target |
| [[NEURL3]] | C | NEURL3 activity raises NOD2's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.23× lower at baseline in the lines without NEURL3 | 0.045 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent; co-absent with the target |
| [[BDKRB2]] | C | BDKRB2 activity raises NOD2's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without BDKRB2 | 0.072 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 22, C 4. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCALD]] | B | NOD2 activity raises NCALD's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.82× lower at baseline in the lines without NOD2 | 0.012 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[CFB]] | B | NOD2 activity raises CFB's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 4.23× lower at baseline in the lines without NOD2 | 0.017 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[RASSF5]] | B | NOD2 activity raises RASSF5's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.83× lower at baseline in the lines without NOD2 | 0.018 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[SULT1C2]] | B | NOD2 activity raises SULT1C2's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.89× lower at baseline in the lines without NOD2 | 0.019 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[SOD2]] | B | NOD2 activity raises SOD2's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without NOD2 | 0.023 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[ELF3]] | B | NOD2 activity raises ELF3's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 2.40× lower at baseline in the lines without NOD2 | 0.035 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[LINC02405]] | B | NOD2 activity raises LINC02405's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 2.31× lower at baseline in the lines without NOD2 | 0.036 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[CYP2J2]] | B | NOD2 activity weakens CYP2J2's drug response | lines that do not express NOD2 (10) vs lines expressing it (25) | the lines without NOD2 respond 1.21× as strongly (z diff -0.51); strongest at Panobinostat 5 µM: 3.88x vs 1.29x (z diff -3.0) | 0.049 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2; target measured in part of the lines; artifact flags |
| [[CARD14]] | B | NOD2 activity raises CARD14's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.53× lower at baseline in the lines without NOD2 | 0.053 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[NINJ1]] | B | NOD2 activity raises NINJ1's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.80× lower at baseline in the lines without NOD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[PSTPIP2]] | B | NOD2 activity raises PSTPIP2's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 2.61× lower at baseline in the lines without NOD2 | 0.067 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[CYLD]] | B | NOD2 activity raises CYLD's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without NOD2 | 0.067 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.6, 3.6); signed map (45.2, 7.5). **Vector** length 59.0, 12.0% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.9 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.5 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.7 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | nucleotide binding oligomerization domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:50,693,588-50,733,077 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BLAU, CD, PSORAS1, CLR16.3, NLRC2; previously IBD1, CARD15 |
| Gene groups (HGNC) | NLR family; Caspase recruitment domain containing |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 35 pathways, smallest: JNK (c-Jun kinases) phosphorylation and  activation mediated by activated human TAK1; activated TAK1 mediates p38 MAPK activation; NOD1/2 Signaling Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC29](https://www.uniprot.org/uniprotkb/Q9HC29) (Nucleotide-binding oligomerization domain-containing protein 2):

> Pattern recognition receptor (PRR) that detects bacterial peptidoglycan fragments and other danger signals and plays an important role in gastrointestinal immunity. Specifically activated by muramyl dipeptide (MDP), a fragment of bacterial peptidoglycan found in every bacterial peptidoglycan type. NOD2 specifically recognizes and binds 6-O-phospho-MDP, the phosphorylated form of MDP, which is generated by NAGK. 6-O-phospho-MDP-binding triggers oligomerization that facilitates the binding and …

**Summary**, from NCBI Gene [64127](https://www.ncbi.nlm.nih.gov/gene/64127):

> This gene is a member of the Nod1/Apaf-1 family and encodes a protein with two caspase recruitment (CARD) domains and six leucine-rich repeats (LRRs). The protein is primarily expressed in the peripheral blood leukocytes. It plays a role in the immune response to intracellular bacterial lipopolysaccharides (LPS) by recognizing the muramyl dipeptide (MDP) derived from them and activating the NFKB protein. Mutations in this gene have been associated with Crohn disease and Blau syndrome. …

**Accessions** — [HGNC:5331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5331) · Entrez [64127](https://www.ncbi.nlm.nih.gov/gene/64127) · UniProt [Q9HC29](https://www.uniprot.org/uniprotkb/Q9HC29) · Ensembl [ENSG00000167207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167207)

## Data

Gene col 9436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9436); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9436]; `tensor/DDL_lfc|DDL_z.npy` [9436]; `embed/gene_vectors.npy` [9436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9436 or target_col == 9436). Every well: [[NOD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
