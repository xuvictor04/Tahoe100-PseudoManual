---
symbol: "PASK"
type: "gene"
col: 3711
ensembl_id: "ENSG00000115687"
name: "PAS domain containing serine/threonine kinase"
location: "2q37.3"
module: 6
arm: "+"
pooled_cpm: 6.56
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PASK

*PAS domain containing serine/threonine kinase* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (20 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.98× (z +22.6, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.590× (z -6.1, q 5e-07, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD54L]] (+0.81, fdr 7e-06), [[XRCC3]] (+0.79, fdr 7e-06), [[TONSL]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.98×** | +22.6 | 0e+00 | 42/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **3.99×** | +16.0 | 0e+00 | 43/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **3.33×** | +13.9 | 9e-42 | 39/46 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **3.07×** | +13.0 | 2e-36 | 39/45 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **2.31×** | +9.3 | 1e-18 | 7/9 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.13×** | +8.4 | 4e-15 | 25/41 (SW480, HT-29, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **2.09×** | +8.2 | 2e-14 | 24/36 (SW480, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.95×** | +7.7 | 8e-13 | 29/46 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.88×** | +7.3 | 2e-11 | 23/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | **1.86×** | +6.9 | 3e-10 | 17/33 (SW480, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.73×** | +6.3 | 1e-08 | 20/42 (LoVo, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.80×** | +6.3 | 1e-08 | 7/15 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.66×** | +5.9 | 2e-07 | 13/28 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.56×** | +5.7 | 5e-07 | 16/43 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +4.4 | 4e-04 | 12/46 (J82, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 12/46 (SW1417, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.023 | 8/46 (BT-474, A549, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.027 | 7/44 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.038 | 9/43 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.044 | 0/46 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.044 | 13/39 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **1.28×** | +2.9 | 0.076 | 4/44 (PANC-1, COLO 205, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3711.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.590×** | -6.1 | 5e-07 | 20/45 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.763×** | -4.4 | 0.003 | 15/44 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.774×** | -4.2 | 0.005 | 12/46 (KATO III, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.734×** | -3.6 | 0.046 | 15/43 (HCT15, RPMI-7951, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.741×** | -3.5 | 0.055 | 17/44 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.735×** | -3.4 | 0.055 | 12/44 (PANC-1, J82, …) | two highest doses | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.766× | -3.1 | 0.16 | 9/46 (A-172, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.19 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.36 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +10.8) | [[Monocrotaline (drug)]] 0.5 µM 0.0455× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 4.52 | 0 | 2 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0507× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 4.56 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +8.6) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0786× (z -9.3) ⚠ cell-cycle shift, explains ~96% of this change |
| [[PANC-1 (line)]] | alt | 8.42 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +12.4) | — |
| [[SW480 (line)]] | alt | 10.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.86× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 6.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 7.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 9.13 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.0645× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 7.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 6.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +10.7) | — |
| [[J82 (line)]] | alt | 8.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +8.9) | — |
| [[LoVo (line)]] | wt | 7.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 2.94 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0771× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 5.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 24.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +10.9) | — |
| [[A-172 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD54L]] | +0.81 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[XRCC3]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[TONSL]] | +0.79 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.78 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[POLE]] | +0.78 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[DDX12P]] | +0.77 | +0.69 / +0.81 | both halves | 7e-06 |  |
| [[E2F2]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[MCM3]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[CLSPN]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[MCM4]] | +0.77 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[MCM5]] | +0.76 | +0.72 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PASK's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[E2F2]] | B | E2F2 activity raises PASK's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.83× lower at baseline in the lines without E2F2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.0, -43.6); signed map (-36.9, -45.6). **Vector** length 77.6, 14.3% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.61 to 65); *DNA strand elongation* (reactome, mean cos +0.64 to 28); *DNA Replication* (reactome, mean cos +0.63 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +22.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | +3.5 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | +3.2 | +6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.0 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +4.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +2.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.4 | +1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.6 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -3.6 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | PAS domain containing serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,106,099-241,150,264 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PASKIN, KIAA0135, STK37 |
| Gene groups (HGNC) | PAS domain containing; PASK family kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RG2](https://www.uniprot.org/uniprotkb/Q96RG2) (PAS domain-containing serine/threonine-protein kinase):

> Serine/threonine-protein kinase involved in energy homeostasis and protein translation. Phosphorylates EEF1A1, GYS1, PDX1 and RPS6. Probably plays a role under changing environmental conditions (oxygen, glucose, nutrition), rather than under standard conditions. Acts as a sensor involved in energy homeostasis: regulates glycogen synthase synthesis by mediating phosphorylation of GYS1, leading to GYS1 inactivation. May be involved in glucose-stimulated insulin production in pancreas and …

**Summary**, from NCBI Gene [23178](https://www.ncbi.nlm.nih.gov/gene/23178):

> This gene encodes a member of the serine/threonine kinase family that contains two PAS domains. Expression of this gene is regulated by glucose, and the encoded protein plays a role in the regulation of insulin gene expression. Downregulation of this gene may play a role in type 2 diabetes. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:17270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17270) · Entrez [23178](https://www.ncbi.nlm.nih.gov/gene/23178) · UniProt [Q96RG2](https://www.uniprot.org/uniprotkb/Q96RG2) · Ensembl [ENSG00000115687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115687)

## Data

Gene col 3711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3711); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3711]; `tensor/DDL_lfc|DDL_z.npy` [3711]; `embed/gene_vectors.npy` [3711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3711 or target_col == 3711). Every well: [[PASK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PASK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
