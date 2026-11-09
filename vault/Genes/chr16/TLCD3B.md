---
symbol: "TLCD3B"
type: "gene"
col: 7416
ensembl_id: "ENSG00000149926"
name: "TLC domain containing 3B"
location: "16p11.2"
module: 71
arm: "+"
pooled_cpm: 2.4
n_lines_expressing: 45
n_dd_up: 17
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 22
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# TLCD3B

*TLC domain containing 3B* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.61× (z +21.7, q 0e+00, up in 23 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.452× (z -7.1, q 8e-10, down in 22 of 39 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.492× (z -6.3, q 7e-08, down in 20 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR19]] (+0.82, fdr 7e-06), [[C21orf58]] (+0.77, fdr 7e-06), [[DMC1]] (+0.77, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 22 go from it, the strongest it → [[C21orf58]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.61×** | +21.7 | 0e+00 | 23/24 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.50×** | +10.7 | 3e-24 | 1/2 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.64×** | +8.3 | 2e-14 | 10/20 (PANC-1, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **2.51×** | +8.2 | 4e-14 | 1/6 (A-172) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.99×** | +6.1 | 1e-07 | 15/39 (A498, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.04×** | +5.8 | 5e-07 | 0/2 | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.82×** | +5.3 | 9e-06 | 10/38 (A498, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.79×** | +5.2 | 2e-05 | 17/38 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.75×** | +5.0 | 4e-05 | 13/39 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.9 | 6e-05 | 6/39 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +4.6 | 2e-04 | 7/27 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.6 | 2e-04 | 12/39 (SHP-77, SW480, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.65×** | +4.5 | 3e-04 | 1/10 (A-427) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.71×** | +4.4 | 4e-04 | 3/16 (SW480, KATO III, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.63×** | +4.2 | 0.001 | 8/25 (MIA PaCa-2, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.452×** | -7.1 | 8e-10 | 22/39 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.492×** | -6.3 | 7e-08 | 20/40 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.505×** | -6.1 | 2e-07 | 19/36 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.548×** | -5.4 | 1e-05 | 12/38 (PANC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.562×** | -5.1 | 3e-05 | 10/27 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.609×** | -4.4 | 9e-04 | 13/39 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -4.4 | 0.001 | 13/15 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.721×** | -4.1 | 0.002 | 12/39 (NCI-H460, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.636×** | -4.0 | 0.003 | 8/38 (SW48, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -4.0 | 0.003 | 15/34 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.649×** | -3.7 | 0.011 | 9/34 (HEC-1-A, PANC-1, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.748×** | -3.7 | 0.011 | 15/36 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.751×** | -3.6 | 0.013 | 9/40 (A498, SW 1271, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.752×** | -3.6 | 0.013 | 14/40 (COLO 205, HCT15, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.680×** | -3.4 | 0.022 | 12/29 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.684×** | -3.4 | 0.025 | 13/37 (A-172, Hs 766T, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.687×** | -3.2 | 0.041 | 7/30 (NCI-H23, A549, …) | rises with dose |  |
| [[Neratinib (drug)]] 0.5 µM |  | **0.702×** | -3.2 | 0.050 | 8/37 (SNU-1, A-427, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.03 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.95 | 0 | 8 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.107× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 4.15 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0840× (z -9.2) |
| [[A-427 (line)]] | wt | 6.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0458× (z -12.1) |
| [[A498 (line)]] | wt | 3.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 1.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +8.7) | — |
| [[SW480 (line)]] | alt | 1.98 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0503× (z -10.2) |
| [[A-172 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.606 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.610 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.834 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.834 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.835 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR19]] | +0.82 | +0.80 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[C21orf58]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[DMC1]] | +0.77 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ASF1B]] | +0.71 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[FBXO43]] | +0.68 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[BRME1]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[RMI2]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[EME1]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[E2F8]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ESCO2]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[BRIP1]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[E2F2]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TLCD3B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[E2F2]] | B | E2F2 activity raises TLCD3B's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without E2F2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf58]] | B | TLCD3B activity raises C21orf58's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.57× lower at baseline in the lines without TLCD3B | 0.007 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[BRCA1]] | B | TLCD3B activity raises BRCA1's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without TLCD3B | 0.014 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[KIF24]] | B | TLCD3B activity raises KIF24's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without TLCD3B | 0.021 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[FANCA]] | B | TLCD3B activity raises FANCA's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without TLCD3B | 0.025 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[DNA2]] | B | TLCD3B activity raises DNA2's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without TLCD3B | 0.032 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[GINS1]] | B | TLCD3B activity raises GINS1's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.47× lower at baseline in the lines without TLCD3B | 0.033 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[SSPOP]] | B | TLCD3B activity raises SSPOP's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.11× lower at baseline in the lines without TLCD3B | 0.042 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[PROCA1]] | B | TLCD3B activity raises PROCA1's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.74× lower at baseline in the lines without TLCD3B | 0.045 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[C5]] | B | TLCD3B activity raises C5's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.45× lower at baseline in the lines without TLCD3B | 0.049 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[POLQ]] | B | TLCD3B activity raises POLQ's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.23× lower at baseline in the lines without TLCD3B | 0.059 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[STIL]] | B | TLCD3B activity raises STIL's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without TLCD3B | 0.069 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[WDR76]] | B | TLCD3B activity raises WDR76's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.23× lower at baseline in the lines without TLCD3B | 0.074 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.2, -47.5); signed map (-41.2, -46.5). **Vector** length 58.6, 9.89% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +21.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +4.2 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +3.7 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +3.2 | +8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.7 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -2.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.9 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | TLC domain containing 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,024,427-30,052,978 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434I2117; previously FAM57B |
| Gene groups (HGNC) | TLC domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q71RH2](https://www.uniprot.org/uniprotkb/Q71RH2) (Ceramide synthase):

> Involved in ceramide synthesis.

**Summary**, from NCBI Gene [83723](https://www.ncbi.nlm.nih.gov/gene/83723):

> This gene encodes a transmembrane protein, which may be a likely target of peroxisome proliferator-activated receptor gamma (PPAR-gamma). The product of the orthologous gene in mouse is related to obesity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:25295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25295) · Entrez [83723](https://www.ncbi.nlm.nih.gov/gene/83723) · UniProt [Q71RH2](https://www.uniprot.org/uniprotkb/Q71RH2) · Ensembl [ENSG00000149926](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149926)

## Data

Gene col 7416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7416); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7416]; `tensor/DDL_lfc|DDL_z.npy` [7416]; `embed/gene_vectors.npy` [7416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7416 or target_col == 7416). Every well: [[TLCD3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLCD3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
