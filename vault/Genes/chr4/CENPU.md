---
symbol: "CENPU"
type: "gene"
col: 7558
ensembl_id: "ENSG00000151725"
name: "centromere protein U"
location: "4q35.1"
module: 6
arm: "+"
pooled_cpm: 34.0
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CENPU

*centromere protein U* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +12.6, q 7e-34, up in 42 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.46× (z +4.4, q 5e-04, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.587× (z -6.2, q 4e-07, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~95% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.733× (z -5.1, q 4e-05, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRIM1]] (+0.85, fdr 7e-06), [[SKA3]] (+0.85, fdr 7e-06), [[FANCI]] (+0.85, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 20 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **2.98×** | +12.6 | 7e-34 | 42/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **2.87×** | +11.7 | 3e-29 | 35/38 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **2.49×** | +10.5 | 1e-23 | 45/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **2.37×** | +10.0 | 3e-21 | 46/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **2.26×** | +9.4 | 4e-19 | 40/48 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **2.20×** | +8.5 | 3e-15 | 34/41 (HOP62, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.77×** | +6.4 | 2e-08 | 32/48 (C32, A549, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.69×** | +5.8 | 4e-07 | 28/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~83% of this change | **1.67×** | +5.7 | 6e-07 | 33/46 (C32, H4, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.40×** | +5.5 | 2e-06 | 28/48 (A-427, SW48, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.55×** | +4.9 | 5e-05 | 27/48 (LOX-IMVI, C32, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~83% of this change | **1.51×** | +4.8 | 9e-05 | 23/46 (RPMI-7951, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.33×** | +4.6 | 2e-04 | 29/48 (HOP62, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 5e-04 | 23/48 (HOP62, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | **1.47×** | +4.3 | 7e-04 | 21/44 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.002 | 25/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.034 | 19/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.29×** | +2.9 | 0.085 | 10/48 (A-427, J82, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 5 µM |  | **1.61×** | +2.9 | 0.097 | 12/48 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7558.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.587×** | -6.2 | 4e-07 | 30/48 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.702×** | -5.8 | 2e-06 | 28/48 (LS 180, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.872× | -5.4 | 1e-05 | 14/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.530×** | -5.2 | 2e-05 | 26/48 (SW480, A-172, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.733×** | -5.1 | 4e-05 | 27/48 (HCT15, RKO, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.679×** | -4.5 | 7e-04 | 22/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.688×** | -4.3 | 0.001 | 27/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.718×** | -3.8 | 0.008 | 25/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.532×** | -3.8 | 0.008 | 24/45 (AsPC-1, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.730×** | -3.4 | 0.033 | 15/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.671×** | -3.3 | 0.049 | 15/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.588×** | -3.2 | 0.062 | 18/48 (Panc 03.27, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.08 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 39.0 | 1 (1 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | [[Selinexor (drug)]] 5 µM 0.240× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 38.8 | 2 (2 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 56.2 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | [[Selinexor (drug)]] 5 µM 0.239× (z -15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Bimiralisib (drug)]] 5 µM 0.108× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 24.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | [[Selinexor (drug)]] 5 µM 0.295× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 46.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +11.0) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[A-172 (line)]] | wt | 42.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.178× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 17.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | — |
| [[C32 (line)]] | wt | 33.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 29.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.110× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 25.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.108× (z -16.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.290× (z -9.0) |
| [[H4 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0947× (z -10.0) ⚠ cell-cycle shift, explains ~95% of this change |
| [[HEC-1-A (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | — |
| [[J82 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.60× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.60× (z +8.5) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | — |
| [[AN3 CA (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRIM1]] | +0.85 | +0.81 / +0.86 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 564 |
| [[SKA3]] | +0.85 | +0.82 / +0.85 | both halves | 7e-06 | STRING 617 |
| [[FANCI]] | +0.85 | +0.82 / +0.83 | both halves | 7e-06 | STRING 604 |
| [[RRM1]] | +0.85 | +0.84 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[ZGRF1]] | +0.84 | +0.82 / +0.84 | both halves | 7e-06 |  |
| [[POLQ]] | +0.84 | +0.84 / +0.81 | both halves | 7e-06 |  |
| [[EXO1]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 548 |
| [[MELK]] | +0.83 | +0.79 / +0.83 | both halves | 7e-06 | STRING 627 |
| [[ATAD2]] | +0.83 | +0.78 / +0.86 | both halves | 7e-06 | STRING 477 |
| [[BLM]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[WDHD1]] | +0.83 | +0.83 / +0.80 | both halves | 7e-06 | STRING 431 |
| [[CENPH]] | +0.83 | +0.85 / +0.84 | both halves | 7e-06 | same gene group; pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises CENPU's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without TCF19 | 0.008 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers CENPU's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises CENPU's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.12× lower at baseline in the lines without E2F8 | 0.068 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CENPU's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without AURKB | 0.035 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises CENPU's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.16× lower at baseline in the lines without MCM10 | 0.045 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[PKMYT1]] | C | PKMYT1 activity raises CENPU's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.53× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises CENPU's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.23× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[BRME1]] | C | BRME1 activity raises CENPU's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without BRME1 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises CENPU's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.52× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.077 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent genes |
| [[MYBL2]] | C | MYBL2 activity raises CENPU's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[SHMT1]] | C | SHMT1 activity raises CENPU's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without SHMT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[CLSPN]] | C | CLSPN activity raises CENPU's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without CLSPN | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.866). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.3, -46.5); signed map (-39.6, -43.9). **Vector** length 120, 40.1% of its response variance represented; |z| ≥ 3 in 1,189 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.65 to 65); *DNA strand elongation* (reactome, mean cos +0.67 to 28); *DNA Replication* (reactome, mean cos +0.67 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | +4.3 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | +4.1 | +11.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +3.8 | +9.4 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +3.7 | +4.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +1.7 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.4 | +4.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +0.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.2 | -5.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -5.7 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -3.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.9 | -3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein U |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:184,694,085-184,734,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CENP-U, KLIP1, CENP-50, PBIP1; previously MLF1IP |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q71F23](https://www.uniprot.org/uniprotkb/Q71F23) (Centromere protein U):

> Component of the CENPA-NAC (nucleosome-associated) complex, a complex that plays a central role in assembly of kinetochore proteins, mitotic progression and chromosome segregation. The CENPA-NAC complex recruits the CENPA-CAD (nucleosome distal) complex and may be involved in incorporation of newly synthesized CENPA into centromeres. Plays an important role in the correct PLK1 localization to the mitotic kinetochores. A scaffold protein responsible for the initial recruitment and maintenance of …

**Summary**, from NCBI Gene [79682](https://www.ncbi.nlm.nih.gov/gene/79682):

> The centromere is a specialized chromatin domain, present throughout the cell cycle, that acts as a platform on which the transient assembly of the kinetochore occurs during mitosis. All active centromeres are characterized by the presence of long arrays of nucleosomes in which CENPA (MIM 117139) replaces histone H3 (see MIM 601128). MLF1IP, or CENPU, is an additional factor required for centromere assembly (Foltz et al., 2006 [PubMed 16622419]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:21348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21348) · Entrez [79682](https://www.ncbi.nlm.nih.gov/gene/79682) · UniProt [Q71F23](https://www.uniprot.org/uniprotkb/Q71F23) · Ensembl [ENSG00000151725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151725)

## Data

Gene col 7558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7558); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7558]; `tensor/DDL_lfc|DDL_z.npy` [7558]; `embed/gene_vectors.npy` [7558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7558 or target_col == 7558). Every well: [[CENPU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
