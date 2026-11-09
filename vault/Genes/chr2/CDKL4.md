---
symbol: "CDKL4"
type: "gene"
col: 12948
ensembl_id: "ENSG00000205111"
name: "cyclin dependent kinase like 4"
location: "2p22.1"
module: 39
arm: "+"
pooled_cpm: 16.09
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# CDKL4

*cyclin dependent kinase like 4* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 1.75× (z +5.4, q 4e-05, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.273× (z -12.7, q 5e-34, down in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.314× (z -5.9, q 2e-07, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOCOS]] (+0.87, fdr 7e-06), [[EPHX3]] (+0.87, fdr 7e-06), [[LINC02803]] (+0.87, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SMCO2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.75×** | +5.4 | 4e-05 | 33/47 (SW480, A549, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.33×** | +4.3 | 0.005 | 29/44 (NCI-H2347, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.51×** | +3.8 | 0.032 | 20/46 (A-172, SW480, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | 1.44× | +3.3 | 0.14 | 19/45 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.2 | 0.14 | 5/47 (NCI-H23, HT-29, …) | inconsistent across doses |  |
| [[Cinacalcet (drug)]] 5 µM |  | 1.38× | +3.1 | 0.16 | 9/47 (PANC-1, SW 1088, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.38× | +3.1 | 0.16 | 17/46 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.37× | +3.0 | 0.17 | 12/46 (hTERT-HPNE, HEC-1-A, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.273×** | -12.7 | 5e-34 | 38/45 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.345×** | -10.0 | 5e-21 | 34/41 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.429×** | -8.2 | 3e-14 | 32/47 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.461×** | -7.6 | 6e-12 | 36/47 (LS 180, SW 900, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.475×** | -7.3 | 4e-11 | 32/47 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.486×** | -7.0 | 2e-10 | 30/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.502×** | -6.7 | 1e-09 | 30/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.489×** | -6.7 | 1e-09 | 27/40 (LOX-IMVI, SW 900, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.314×** | -5.9 | 2e-07 | 29/47 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.572×** | -5.5 | 3e-06 | 27/44 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.561×** | -5.4 | 3e-06 | 30/46 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.582×** | -5.3 | 6e-06 | 27/46 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.647×** | -4.3 | 9e-04 | 24/44 (KATO III, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.671×** | -3.7 | 0.009 | 19/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **0.506×** | -3.5 | 0.019 | 15/44 (RKO, H4, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.700×** | -3.4 | 0.028 | 23/46 (PANC-1, LoVo, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.704×** | -3.3 | 0.032 | 11/46 (AN3 CA, A549, …) | top dose only | plate-row cell shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.703×** | -3.3 | 0.035 | 18/46 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bexarotene (drug)]] 5 µM |  | **0.721×** | -3.2 | 0.036 | 16/47 (NCI-H2030, A-172, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.722×** | -3.2 | 0.036 | 13/46 (PANC-1, J82, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.797×** | -3.2 | 0.039 | 21/47 (NCI-H2030, RKO, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.059 | 14/47 (NCI-H1573, H4, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -2.9 | 0.080 | 20/46 (LOX-IMVI, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 44.3 | 0 | 9 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0675× (z -17.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 11.2 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.121× (z -12.4) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HepG2_C3A (line)]] | wt | 44.7 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0564× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.102× (z -12.2) |
| [[PANC-1 (line)]] | alt | 14.7 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.122× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.215× (z -8.5) |
| [[A-427 (line)]] | wt | 14.9 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0772× (z -12.0) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H460 (line)]] | wt | 18.2 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.164× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 16.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 9.30 | 0 | 2 (1 ⚠) | — | [[Brimonidine (drug)]] 0.5 µM 0.0672× (z -9.4) |
| [[C-33 A (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Methotrexate (drug)]] 0.05 µM 0.0482× (z -12.5) |
| [[KATO III (line)]] | alt | 14.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 17.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 30.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0198× (z -23.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0918× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0165× (z -9.1) |
| [[SW 900 (line)]] | alt | 49.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.105× (z -8.8) ⚠ toxic |
| [[C32 (line)]] | wt | 14.1 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0685× (z -10.2) |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0804× (z -10.3) ⚠ toxic |
| [[H4 (line)]] | wt | 21.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.125× (z -8.5) |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0939× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.158× (z -12.2) |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 8.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0843× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOCOS]] | +0.87 | +0.88 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[EPHX3]] | +0.87 | +0.84 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[LINC02803]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[SLC22A14]] | +0.85 | +0.86 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[OIT3]] | +0.84 | +0.84 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.82 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.81 | +0.78 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[IDI2-AS1]] | +0.81 | +0.84 / +0.70 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.81 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.81 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.80 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[MPP4]] | +0.80 | +0.80 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMCO2]] | B | SMCO2 activity raises CDKL4's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.33× lower at baseline in the lines without SMCO2 | 0.006 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[SPOCK2]] | B | SPOCK2 activity raises CDKL4's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without SPOCK2 | 0.051 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises CDKL4's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without C21orf91-OT1 | 0.066 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[SLC22A20P]] | C | SLC22A20P activity raises CDKL4's level | lines that do not express SLC22A20P (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without SLC22A20P | 0.082 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CDC42EP1, PLEKHG5, MYH16; maybe low, not absent |
| [[MPP4]] | C | MPP4 activity raises CDKL4's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 2.53× lower at baseline in the lines without MPP4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.886). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.9, -14.7); signed map (16.8, 8.8). **Vector** length 112, 29.3% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.5 | +1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.2 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.0 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.3 | +2.4 |
| fall | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -5.2 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.4 | -3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -12.7 |
|  | [[NG25 (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -5.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:39,168,045-39,243,983 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cyclin dependent kinase like family |
| Matched by | ensembl_id |

UniProt [Q5MAI5](https://www.uniprot.org/uniprotkb/Q5MAI5) carries no function annotation.

**Summary**, from NCBI Gene [344387](https://www.ncbi.nlm.nih.gov/gene/344387):

> Predicted to enable protein serine/threonine kinase activity. Predicted to be involved in regulation of cell cycle. Predicted to be located in cytoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19287) · Entrez [344387](https://www.ncbi.nlm.nih.gov/gene/344387) · UniProt [Q5MAI5](https://www.uniprot.org/uniprotkb/Q5MAI5) · Ensembl [ENSG00000205111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205111)

## Data

Gene col 12948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12948); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12948]; `tensor/DDL_lfc|DDL_z.npy` [12948]; `embed/gene_vectors.npy` [12948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12948 or target_col == 12948). Every well: [[CDKL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
