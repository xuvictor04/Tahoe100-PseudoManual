---
symbol: "IQGAP3"
type: "gene"
col: 11467
ensembl_id: "ENSG00000183856"
name: "IQ motif containing GTPase activating protein 3"
location: "1q22"
module: 67
arm: "+"
pooled_cpm: 59.03
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 32
n_dd_up_clean: 3
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# IQGAP3

*IQ motif containing GTPase activating protein 3* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.49× (z +4.8, q 0.001, up in 30 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.38× (z +3.7, q 0.026, up in 22 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.381× (z -16.3, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIT]] (+0.86, fdr 7e-06), [[KIFC1]] (+0.85, fdr 7e-06), [[CENPI]] (+0.85, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11467.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.49×** | +4.8 | 0.001 | 30/46 (LoVo, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.42×** | +4.1 | 0.009 | 18/39 (Panc 03.27, AsPC-1, …) | rises with dose | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.40×** | +4.1 | 0.009 | 25/45 (H4, HT-29, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.026 | 22/45 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.073 | 18/45 (HT-29, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.091 | 20/45 (SHP-77, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.30× | +3.2 | 0.13 | 16/45 (HT-29, H4, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11467.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.381×** | -16.3 | 0e+00 | 42/46 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.394×** | -11.1 | 3e-26 | 42/46 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.516×** | -7.9 | 5e-13 | 32/46 (KATO III, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.532×** | -7.3 | 6e-11 | 37/46 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.359×** | -6.4 | 2e-08 | 28/42 (SHP-77, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -6.2 | 5e-08 | 28/46 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.577×** | -6.2 | 5e-08 | 30/46 (HOP62, KATO III, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.605×** | -5.9 | 2e-07 | 36/46 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.615×** | -5.8 | 5e-07 | 29/46 (MIA PaCa-2, A-427, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.714×** | -5.7 | 8e-07 | 36/46 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.629×** | -5.5 | 2e-06 | 28/46 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.620×** | -5.5 | 2e-06 | 30/44 (A549, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -5.0 | 2e-05 | 25/46 (HOP62, NCI-H2347, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.661×** | -4.9 | 3e-05 | 34/46 (LoVo, SNU-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.755×** | -4.7 | 9e-05 | 23/46 (LS 180, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.680×** | -4.6 | 2e-04 | 26/46 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.770×** | -4.4 | 4e-04 | 23/46 (H4, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.780×** | -4.2 | 9e-04 | 24/46 (HEC-1-A, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.514×** | -4.2 | 9e-04 | 26/46 (SW1417, SW 900, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 100 | 0 | 9 (3 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.142× (z -14.3) |
| [[LS 180 (line)]] | wt | 47.4 | 0 | 8 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.107× (z -18.3) |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -14.0) |
| [[A549 (line)]] | wt | 43.7 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.189× (z -17.2) |
| [[HOP62 (line)]] | alt | 161 | 0 | 7 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.318× (z -12.7) |
| [[A498 (line)]] | wt | 81.1 | 0 | 6 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.143× (z -20.0) |
| [[HEC-1-A (line)]] | alt | 85.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 41.4 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0748× (z -16.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.161× (z -16.0) |
| [[A-172 (line)]] | wt | 120 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.222× (z -15.7) |
| [[A-427 (line)]] | wt | 62.8 | 0 | 5 | — | [[Selinexor (drug)]] 5 µM 0.247× (z -14.9) |
| [[C32 (line)]] | wt | 92.7 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.231× (z -13.5) |
| [[KATO III (line)]] | alt | 50.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -16.1) |
| [[LoVo (line)]] | wt | 41.5 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.274× (z -13.9) |
| [[Hs 766T (line)]] | wt | 38.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.2) |
| [[HT-29 (line)]] | alt | 40.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 48.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 52.3 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.288× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 31.8 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.158× (z -17.0) |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -12.8) |
| [[SW480 (line)]] | alt | 32.5 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.276× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 55.5 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.155× (z -16.7) |
| [[NCI-H23 (line)]] | alt | 109 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 53.5 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.371× (z -11.8) |
| [[AN3 CA (line)]] | alt | 51.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.114× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 44.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.176× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 47.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +12.3) | — |
| [[RPMI-7951 (line)]] | alt | 59.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.327× (z -9.2) |
| [[SHP-77 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0375× (z -12.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 56.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.285× (z -11.3) |
| [[SW48 (line)]] | wt | 58.6 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.355× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIT]] | +0.86 | +0.85 / +0.84 | both halves | 7e-06 | pathway: RAC1 GTPase cycle; STRING 502 |
| [[KIFC1]] | +0.85 | +0.82 / +0.85 | both halves | 7e-06 | STRING 450 |
| [[CENPI]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[AURKB]] | +0.84 | +0.83 / +0.79 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 427 |
| [[CEP55]] | +0.83 | +0.77 / +0.80 | both halves | 7e-06 | STRING 422 |
| [[TACC3]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 |  |
| [[SPAG5]] | +0.82 | +0.82 / +0.81 | both halves | 7e-06 | STRING 558 |
| [[RACGAP1]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 | pathway: CDC42 GTPase cycle; STRING 414 |
| [[NCAPG2]] | +0.80 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[KIF22]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[SPC25]] | +0.80 | +0.78 / +0.80 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[PBK]] | +0.80 | +0.79 / +0.76 | both halves | 7e-06 | STRING 475 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises IQGAP3's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PIMREG]] | B | PIMREG activity raises IQGAP3's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.37× lower at baseline in the lines without PIMREG | 0.043 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises IQGAP3's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.32× lower at baseline in the lines without PBK | 0.035 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises IQGAP3's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.79× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.4, -53.6); signed map (-46.8, -41.9). **Vector** length 150, 53.2% of its response variance represented; |z| ≥ 3 in 1,355 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.73 to 12); *G2/M checkpoint* (hallmark, mean cos +0.74 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.70 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.3 | +4.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.4 | +1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | +1.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.2 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[vincristine (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.6 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.6 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.4 | -16.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -9.6 | -11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -7.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.7 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -3.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif containing GTPase activating protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,525,405-156,572,604 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | IQ motif containing GTPase activating protein family |
| Reactome | 12 pathways, smallest: RHO GTPases activate IQGAPs; RHOJ GTPase cycle; RHOQ GTPase cycle |
| Matched by | ensembl_id |

UniProt [Q86VI3](https://www.uniprot.org/uniprotkb/Q86VI3) carries no function annotation.

**Summary**, from NCBI Gene [128239](https://www.ncbi.nlm.nih.gov/gene/128239):

> Enables calmodulin binding activity and myosin VI light chain binding activity. Predicted to be involved in mitotic actomyosin contractile ring assembly actin filament organization. Predicted to act upstream of or within several processes, including G1/S transition of mitotic cell cycle; intracellular signaling cassette; and regulation of gene expression. Predicted to be located in cytosol. Predicted to be active in cell cortex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20669) · Entrez [128239](https://www.ncbi.nlm.nih.gov/gene/128239) · UniProt [Q86VI3](https://www.uniprot.org/uniprotkb/Q86VI3) · Ensembl [ENSG00000183856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183856)

## Data

Gene col 11467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11467); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11467]; `tensor/DDL_lfc|DDL_z.npy` [11467]; `embed/gene_vectors.npy` [11467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11467 or target_col == 11467). Every well: [[IQGAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQGAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
