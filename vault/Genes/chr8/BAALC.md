---
symbol: "BAALC"
type: "gene"
col: 9032
ensembl_id: "ENSG00000164929"
name: "BAALC binder of MAP3K1 and KLF4"
location: "8q22.3"
module: 13
arm: "+"
pooled_cpm: 5.86
n_lines_expressing: 18
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 38
direction_downstream: 53
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# BAALC

*BAALC binder of MAP3K1 and KLF4* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.15× (z +17.4, q 0e+00, up in 9 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.564× (z -4.9, q 2e-04, down in 5 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01060]] (+0.74, fdr 7e-06), [[GDNF-AS1]] (+0.68, fdr 7e-06), [[PDE3A]] (+0.66, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 53 go from it, the strongest it → [[SEMA6D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.15×** | +17.4 | 0e+00 | 9/13 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +13.1 | 8e-37 | 3/12 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.41×** | +12.3 | 1e-32 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +9.6 | 1e-19 | 2/10 (A498, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +8.4 | 4e-15 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.12×** | +6.5 | 9e-09 | 4/12 (HEC-1-A, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +6.2 | 4e-08 | 6/12 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.7 | 2e-04 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.66×** | +4.4 | 6e-04 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.9 | 0.006 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Flutamide (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.009 | 0/13 | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.021 | 1/12 (SHP-77) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.021 | 2/14 (HEC-1-A, SK-MEL-2) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.021 | 3/15 (HS-578T, SW 1088, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.084 | 2/13 (HS-578T, hTERT-HPNE) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.564×** | -4.9 | 2e-04 | 5/13 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.565×** | -4.9 | 2e-04 | 9/14 (hTERT-HPNE, SHP-77, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.621×** | -4.1 | 0.007 | 7/12 (hTERT-HPNE, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.558×** | -3.9 | 0.011 | 6/13 (hTERT-HPNE, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.642×** | -3.8 | 0.014 | 7/13 (HOP62, RPMI-7951, …) | two highest doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.610×** | -3.7 | 0.024 | 1/13 (A-172) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.631×** | -3.4 | 0.052 | 1/13 (HOP62) | inconsistent across doses |  |
| [[LB-100 (drug)]] 0.05 µM |  | 0.678× | -3.2 | 0.11 | 1/15 (AN3 CA) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 150 | 0 | 14 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0266× (z -18.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -15.0) |
| [[SHP-77 (line)]] | alt | 86.4 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -15.1) |
| [[A-172 (line)]] | wt | 5.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 51.8× (z +17.1) | — |
| [[RPMI-7951 (line)]] | alt | 26.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0450× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -9.5) |
| [[A498 (line)]] | wt | 1.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 3.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0757× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 4.26 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 42.4× (z +8.7) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[SNU-423 (line)]] | alt | 2.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.4× (z +12.0) | — |
| [[A-427 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.820 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.925 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.788 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01060]] | +0.74 | +0.67 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[GDNF-AS1]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[PDE3A]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTSL1]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 | same gene group |
| [[ANGPTL2]] | +0.64 | +0.53 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[ABCA13]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[SYNDIG1]] | +0.63 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[KCNE4]] | +0.63 | +0.55 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[OFCC1]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CARMN]] | +0.63 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[LDB2]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[APCDD1L-DT]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 2, C 36. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises BAALC's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers BAALC's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PDZRN3]] | C | PDZRN3 activity raises BAALC's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 3.10× lower at baseline in the lines without PDZRN3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises BAALC's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 4.29× lower at baseline in the lines without KCNE4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[HGF]] | C | HGF activity raises BAALC's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.35× lower at baseline in the lines without HGF | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises BAALC's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 2.98× lower at baseline in the lines without SPOCK1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises BAALC's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.61× lower at baseline in the lines without SYT4 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises BAALC's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 3.53× lower at baseline in the lines without ITGA11 | 0.006 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[TEX41]] | C | TEX41 activity raises BAALC's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 2.93× lower at baseline in the lines without TEX41 | 0.007 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises BAALC's level | lines that do not express GDNF (38) vs lines expressing it (12) | 4.39× lower at baseline in the lines without GDNF | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[LINC02492]] | C | LINC02492 activity raises BAALC's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 2.43× lower at baseline in the lines without LINC02492 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent; co-absent with the target |
| [[CSF1R]] | C | CSF1R activity raises BAALC's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 2.78× lower at baseline in the lines without CSF1R | 0.012 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 12, C 41. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6D]] | B | BAALC activity raises SEMA6D's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.95× lower at baseline in the lines without BAALC | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[CFAP20DC-DT]] | B | BAALC activity raises CFAP20DC-DT's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.90× lower at baseline in the lines without BAALC | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[OFCC1]] | B | BAALC activity raises OFCC1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.82× lower at baseline in the lines without BAALC | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[RNF152]] | B | BAALC activity raises RNF152's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.47× lower at baseline in the lines without BAALC | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[RETREG1-AS1]] | B | BAALC activity raises RETREG1-AS1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.20× lower at baseline in the lines without BAALC | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[LRIG1]] | B | BAALC activity raises LRIG1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.86× lower at baseline in the lines without BAALC | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[LDB2]] | B | BAALC activity raises LDB2's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.34× lower at baseline in the lines without BAALC | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[PECAM1]] | B | BAALC activity raises PECAM1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.00× lower at baseline in the lines without BAALC | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[LINC02257]] | B | BAALC activity raises LINC02257's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.04× lower at baseline in the lines without BAALC | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[VENTXP1]] | B | BAALC activity raises VENTXP1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.74× lower at baseline in the lines without BAALC | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[CNTNAP4]] | B | BAALC activity raises CNTNAP4's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.79× lower at baseline in the lines without BAALC | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[SNCAIP]] | B | BAALC activity raises SNCAIP's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.72× lower at baseline in the lines without BAALC | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.6, 20.6); signed map (23.2, 46.9). **Vector** length 52.1, 17.0% of its response variance represented; |z| ≥ 3 in 388 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +17.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | BAALC binder of MAP3K1 and KLF4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:103,140,713-103,230,305 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXS3](https://www.uniprot.org/uniprotkb/Q8WXS3) (Brain and acute leukemia cytoplasmic protein):

> May play a synaptic role at the postsynaptic lipid rafts possibly through interaction with CAMK2A.

**Summary**, from NCBI Gene [79870](https://www.ncbi.nlm.nih.gov/gene/79870):

> This gene was identified by gene expression studies in patients with acute myeloid leukemia (AML). The gene is conserved among mammals and is not found in lower organisms. Tissues that express this gene develop from the neuroectoderm. Multiple alternatively spliced transcript variants that encode different proteins have been described for this gene; however, some of the transcript variants are found only in AML cell lines. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14333](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14333) · Entrez [79870](https://www.ncbi.nlm.nih.gov/gene/79870) · UniProt [Q8WXS3](https://www.uniprot.org/uniprotkb/Q8WXS3) · Ensembl [ENSG00000164929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164929)

## Data

Gene col 9032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9032); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9032]; `tensor/DDL_lfc|DDL_z.npy` [9032]; `embed/gene_vectors.npy` [9032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9032 or target_col == 9032). Every well: [[BAALC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAALC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
